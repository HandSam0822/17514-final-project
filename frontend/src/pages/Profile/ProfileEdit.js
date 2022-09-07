import { Button, Form } from 'react-bootstrap/';
import React, { useState } from 'react';
import { post, onSuccessOrFail, redirect, ReadEasyDate } from 'utils/sdk';
import { convertToBase64 } from './sdk';
// import { notifyError } from 'utils/notification';
import { BACKEND_IMAGE_URL } from 'constants/url';
import 'styles/profile.css';
import { useSelector } from 'react-redux';
import { editProfile } from 'actions/allActions';
import { useDispatch } from 'react-redux';

export function ProfileEdit() {
  const my_username = useSelector((state) => state.username);
  const id = useSelector((state) => state.id);
  const date_joined = useSelector((state) => state.date_joined);
  const bio = useSelector((state) => state.bio);
  const location = useSelector((state) => state.location);

  const dispatch = useDispatch();
  const [profileData, setProfileData] = useState({
    username: my_username,
    bio: bio,
    location: location,
    created_at: date_joined
  });

  const handleChange = (e) => {
    const id = e.target.id;
    const value = e.target.value;
    setProfileData((prevValue) => {
      return {
        ...prevValue,
        [id]: value
      };
    });
  };

  const [postImage, setPostImage] = useState({
    image: ''
  });
  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    const base64 = await convertToBase64(file);
    setPostImage({ ...postImage, image: base64 });
  };

  const savedProfile = () => {
    post(`profile/${my_username}`, { ...profileData, ...postImage })
      .then((resp) => onSuccessOrFail(resp, null))
      .then((resp) => {
        if (!resp) {
          redirect('/error');
        }
      })
      .then(dispatch(editProfile(profileData)))
      .then(window.location.reload());
  };

  return (
    <div className="profile" style={{ marginLeft: '300px', fontFamily: "Helvetica" }}>
      <h1>Edit your myCMU profile</h1>
      <div style={{ marginBottom: '60px' }}>
        <label htmlFor="image">
          <input
            type="file"
            accept=".jpeg, .png, .jpg"
            name="image"
            id="image"
            style={{ display: 'none' }}
            onChange={(e) => handleFileUpload(e)}
          />
          <img alt="" src={`${BACKEND_IMAGE_URL}${my_username}.png`}></img>
        </label>
      </div>
      <Button variant="primary" onClick={() => savedProfile()}>
        Save
      </Button>
      <Form>
        <Form.Group className="mb-3" controlId="username">
          <Form.Label>user name</Form.Label>
          <Form.Control
            type="text"
            onChange={(e) => handleChange(e)}
            value={profileData.username}
            readOnly
            disabled
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
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="location">
          <Form.Label>location</Form.Label>
          <Form.Control
            size="lg"
            type="text"
            onChange={(e) => handleChange(e)}
            value={profileData.location}
          />
        </Form.Group>

        <Form.Group className="mb-3" controlId="created_at">
          <Form.Label>created at</Form.Label>
          <Form.Control
            readOnly
            type="text"
            onChange={(e) => handleChange(e)}
            value={ReadEasyDate(profileData.created_at)}
          />
        </Form.Group>
      </Form>
    </div>
  );
}
