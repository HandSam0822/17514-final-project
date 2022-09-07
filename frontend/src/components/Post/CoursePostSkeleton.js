import React, { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import { redirect, ReadEasyDate, DisplayDetail, stringEqual } from 'utils/sdk';
import { BACKEND_IMAGE_URL, DEFAULT_IMAGE_URL } from 'constants/url';
import MainContainer from 'components/MainContainer';
import LeftContainer from 'components/LeftContainer';
import RightContainer from 'components/RightContainer';
import { DropdownButton, Dropdown } from 'react-bootstrap';
import { deletePost, getCoursePostData, getCoursePostDataWithFilter } from 'utils/crud';
import { Form } from 'react-bootstrap';
// import saved from 'icon/saved.png' // relative path to image
import { SearchIcon } from 'components/Icon';
import 'styles/post.css';
import $ from 'jquery';

// Ref: https://react-bootstrap.github.io/components/dropdowns/
/**
 * Render a list of basic info of coursePost, if user want to check detail, it should click
 * the "read more" button to go to specific post.
 * @param {*} props
 * @returns
 */

export const CoursePostSkeleton = () => {
  let [coursePosts, setCoursePosts] = useState([]);
  // let [postFollowingStatus, setPostFollowingStatus] = useState([]);
  const [searchData, setSearchData] = useState({
    title: '',
    text: '',
    username: '',
    sort: 'update_time'
  });

  $('.dropdown-item').on('click', function () {
    const text = $(this).text();
    setSearchData((prevValue) => {
      return {
        ...prevValue,
        sort: text
      };
    });
    console.log($(this).text());
  });

  const handleChange = (e) => {
    const id = e.currentTarget.id;
    const value = e.target.value;
    setSearchData((prevValue) => {
      return {
        ...prevValue,
        [id]: value
      };
    });
    console.log(searchData);
  };

  const handleDelete = (deletePostId, type) => {
    let res = deletePost(deletePostId, type);
    if (res) {
      setCoursePosts(coursePosts.filter((post) => post.id !== deletePostId));
    }
  };

  /** for initial statement */
  useEffect(() => {
    getCoursePostData().then((data) => {
      setCoursePosts(data.post);
    });
  }, []);

  /**for delete a post */
  useEffect(() => {
    setCoursePosts(coursePosts);
  }, [coursePosts]);

  /** for user wanna make a search and searchData's value is changed  */
  useEffect(() => {
    getCoursePostDataWithFilter(searchData).then((posts) => setCoursePosts(posts));
    console.log('make a request');
  }, [searchData]);

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
      <div className="post-content" onClick={() => redirect('coursePost/' + post.id.toString())}>
        <div className="post-content-header">
          <div>
            {post.course_post_user.username} post on course
            <span>
              <a className="" href={`./course/search/${post.course_id.id}`}>
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
        </DropdownButton>                
      </div>
    </div>
  ));

  return (
    <MainContainer>
      <LeftContainer>
        <Form className="search-form">
          <SearchIcon />
          <Form.Group className="mb-3" controlId="title">
            <Form.Control
              onChange={(e) => handleChange(e)}
              type="text"
              autoComplete="off"
              placeholder="title"
            />
          </Form.Group>

          <Form.Group className="mb-3" controlId="text">
            <Form.Control
              onChange={(e) => handleChange(e)}
              type="text"
              autoComplete="off"
              placeholder="text"
            />
          </Form.Group>

          <Form.Group className="mb-3" controlId="username">
            <Form.Control
              onChange={(e) => handleChange(e)}
              type="username"
              autoComplete="off"
              placeholder="username"
            />
          </Form.Group>
          
          <DropdownButton style={{marginLeft: "15px"}} title={searchData.sort}>
            <Dropdown.Item disabled>Select order</Dropdown.Item>
            <Dropdown.Item >update_time</Dropdown.Item>
            <Dropdown.Item>followers</Dropdown.Item>
            <Dropdown.Item>name</Dropdown.Item>
          </DropdownButton>
        </Form>

        {listItems}
      </LeftContainer>
      <RightContainer></RightContainer>
    </MainContainer>
  );
};


