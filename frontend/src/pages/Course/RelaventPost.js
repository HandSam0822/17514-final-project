import React, { useEffect, useState } from 'react'
import MainContainer from 'components/MainContainer'
import LeftContainer from 'components/LeftContainer'
import RightContainer from 'components/RightContainer'
import { get_url_param_last } from 'utils/sdk'
import { deletePost, getMentionCourseByCourseId } from 'utils/crud'
import { useSelector } from 'react-redux';
import { redirect, ReadEasyDate, DisplayDetail, stringEqual } from 'utils/sdk';
import { BACKEND_IMAGE_URL, DEFAULT_IMAGE_URL } from 'constants/url';
import { DropdownButton, Dropdown } from 'react-bootstrap';
import 'styles/post.css';

/** get all course that is relavent to a specific course */
const RelaventPost = () => {
    const id = get_url_param_last()
    let [coursePosts, setCoursePosts] = useState([]);

 /** for initial statement */
 useEffect(() => {
    getMentionCourseByCourseId(id).then((data) => {
      setCoursePosts(data.post);
    });
  }, []);


  const handleDelete = (deletePostId, type) => {
    let res = deletePost(deletePostId, type);
    if (res) {
      setCoursePosts(coursePosts.filter((post) => post.id !== deletePostId));
    }
  };
  const username = useSelector((state) => state.username);
  let listItems = coursePosts.length === 0 ? <h2>😌 no matching post</h2> : coursePosts.map((post, index) => (
    <div key={post.id} className="post">
      <div className="post-icon">
        <object
          onClick={() => {
            redirect(`profile/${post.course_post_user.username}`);
          }}
          data={`${BACKEND_IMAGE_URL}${post.course_post_user.username}.png`}
          type="image/png">
          <img
            onClick={() => {
              redirect(`profile/${post.course_post_user.username}`);
            }}
            alt=""
            src={DEFAULT_IMAGE_URL}></img>
        </object>
      </div>
      <div className="post-content" onClick={() => redirect('/coursePost/' + post.id.toString())}>
        <div className="post-content-header">
          <div>
            {post.course_post_user.username} post on course
            <span>
              <a className="" href={`./course/search/${post.course_id.course_number}`}>
                {post.course_id.course_number}
              </a>
            </span>
            <span className="time-span">
              {ReadEasyDate(post.creation_time)}
              <span className="hide">{DisplayDetail(post.creation_time)}</span>
            </span>
          </div>
        </div>
        <div className="post-content-text">
          <span>{post.course_post_title}</span>
        </div>
      </div>

      <div className="post-option">
        <DropdownButton id="dropdown-button" size="sm" title="">
          {stringEqual(post.course_post_user.username, username) ? (
            <Dropdown.Item id="dropdown-item" onClick={() => handleDelete(post.id, 'course_post')}>
              delete
            </Dropdown.Item>
          ) : null}
          {stringEqual(post.course_post_user.username, username) ? (
            <Dropdown.Item
              id="dropdown-item"
              onClick={() => redirect(`/coursePost/${post.id}/edit`)}>
              edit
            </Dropdown.Item>
          ) : null}
          <Dropdown.Item id="dropdown-item" onClick={() => console.log('clock')}>
            follow
          </Dropdown.Item>
        </DropdownButton>                
      </div>
    </div>
  ));
  
  return ( 
    <MainContainer>
    <LeftContainer>     
      {listItems}
    </LeftContainer>
    <RightContainer></RightContainer>
  </MainContainer>
  )
}

export default RelaventPost