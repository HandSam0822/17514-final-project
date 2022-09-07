import { Button, Form } from 'react-bootstrap/';
import React, { useState, useEffect } from 'react';
import { get, isErrorClass, post, ReadEasyDate, redirect } from 'utils/sdk';
import { notifyError } from 'utils/notification';
import { BACKEND_IMAGE_URL, DEFAULT_IMAGE_URL } from 'constants/url';
import 'styles/profile.css';
import { get_url_param_last } from 'utils/sdk';
import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import {EditButton, FollowUnfollowButton} from './Button'
function Profile() {
  const my_username = useSelector((state) => state.username);
  const id = useSelector((state) => state.id);
  const date_joined = useSelector((state) => state.date_joined);
  const bio = useSelector((state) => state.bio);
  const location = useSelector((state) => state.location);
  const search_user = get_url_param_last();
  const is_myself = my_username == search_user;
  const [email, setEmail] = useState(useSelector((state) => state.email)) 
  const [profileData, setProfileData] = useState({
    user_name: search_user,
    bio: bio,
    location: location,
    created_at: date_joined,
    email: email
  });
  const [isFollowing, setIsFollowing] = useState(false);  
  const [imageurl, setImageurl] = useState(`${BACKEND_IMAGE_URL}${my_username}.png`);
  const nav = useNavigate();
  const handleChange = (e) => {
    const id = e.target.id;
    const value = e.target.value;
    setProfileData((prevValue) => {
      return {
        ...prevValue,
        [id]: value
      };
    });
    console.log(profileData);
  };

  useEffect(() => {
    if (!is_myself) {
      get(`profile/${search_user}`)
        .then((resp) => {
          if (isErrorClass(resp)) {
            // should be route to different error page
            redirect('/error');
          } else {
            // don't use profileData because it is async
            if (resp.data.profile.profile_picture)
              setImageurl(`${BACKEND_IMAGE_URL}${resp.data.profile.profile_picture}`);
            else setImageurl(DEFAULT_IMAGE_URL);            
            setProfileData(resp.data.profile);            
            setIsFollowing(resp.data.is_following);
            setEmail(resp.data.email)
          }
        })
        .catch((error) => notifyError(error));
    }
  }, []);
  
  const handleClick = () => {
    post(`profile/${search_user}`);
    setIsFollowing(!isFollowing);
  }
  return ( 
    <div className="profile" style={{ marginLeft: '300px' }}>
      <div style={{ marginBottom: '60px' }}>
        <img onClick={() => nav('photo')} alt="" src={imageurl}></img>
      </div>
     {is_myself ? <EditButton ></EditButton> : 
     <FollowUnfollowButton following = {isFollowing} 
     onClick={()=>handleClick()}/>}
      <Form>
        <Form.Group className="mb-3" controlId="email">
          <Form.Label>Email address</Form.Label>
          <Form.Control
            type="email"
            //should later change to insta or other link that serialize from profile
            placeholder={profileData.email}
            onChange={(e) => handleChange(e)}
            value={email}
            disabled
            readOnly
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="user_name">
          <Form.Label>user name</Form.Label>
          <Form.Control
            type="text"
            onChange={(e) => handleChange(e)}
            value={profileData.user_name}
            disabled
            readOnly
          />
        </Form.Group>
        <Form.Group className="mb-3" controlId="bio">
          <Form.Label>About</Form.Label>
          <Form.Control
            as="textarea"
            rows={3}
            placeholder="Tell us about yourself so CMU community could know you more."
            onChange={(e) => handleChange(e)}
            value={profileData.bio}
            disabled
            readOnly
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="location">
          <Form.Label>location</Form.Label>
          <Form.Control
            size="lg"
            type="text"
            onChange={(e) => handleChange(e)}
            value={profileData.location}
            disabled
            readOnly
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="created_at">
          <Form.Label>created at</Form.Label>
          <Form.Control
            
            type="text"
            onChange={(e) => handleChange(e)}
            value={ReadEasyDate(profileData.created_at)}
            disabled
            readOnly
          />
        </Form.Group>
      </Form>
    </div>
  );
}

export default Profile;
