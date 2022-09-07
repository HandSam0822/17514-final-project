import React, { useEffect, useState } from 'react';
import { get, get_url_param_last, isErrorClass, redirect } from 'utils/sdk';
import { Form, Button } from 'react-bootstrap';
import { notifyError } from 'utils/notification';
import {
  follow_unfollow_course_post,
  postCourseComment
} from 'utils/crud';
import { onSuccessOrFail } from 'utils/sdk';
import { SavedIcon, UnsavedIcon } from 'components/Icon';
import { DisplayDetail } from 'utils/sdk';


const CoursePostDetail = () => {
  const [post, setPost] = useState({});
  const [following, setFollowing] = useState(false);
  const [post_comments, set_post_comments] = useState([]);
  
  const id = get_url_param_last();
  useEffect(() => {

  get(`course_post_comment_by_postid/${id}`)
  .then(resp => {         
    if (isErrorClass(resp)) {
      notifyError(resp.message)          
    } else {        
      let data = resp.data;      
      set_post_comments(data.comments)
    }     
  })    

  get(`course_post/${id}`)
  .then((resp) => onSuccessOrFail(resp, null, false))
  .then((resp) => {
    if (resp) {
      let data = resp.data;
      setPost(data.post);
      setFollowing(data.following)
       

    } else {
      redirect('/error');
    }
  });
  
}, []);




  const [message, setMessage] = useState('');
  const handleFollowingClick = () => {
    follow_unfollow_course_post(id);
    setFollowing(!following);
  };

  let listItems = post_comments.map((comment) =>  
    <div key={comment.id} className="" style={{padding: "0.5rem"}}>
    <div>comment text: {comment.course_comment_text}</div>
    <div>by: {comment.course_comment_text.username ? comment.course_comment_text.username : null}</div>
    <div>time: {DisplayDetail(comment.creation_time)}</div>  
    </div>   
  )
  console.log(listItems)
  return (
    <>
      <div
        key={post.id}
        className=""
        style={{ padding: '0.5rem', marginLeft: '350px', fontFamily: "Helvetica"}}>
        <h3>this is course post part</h3>
        <div style={{fontWeight: 'bold'}}>Post id: {post.id} created @  {DisplayDetail(post.creation_time)}</div>
        <br></br>
        <h2>{post.course_post_title}</h2>
        <div>{post.course_post_text}</div>
        
        <div style={{marginTop: '2rem'}}> 
        
        {listItems}
        <Form>
          <Form.Group className="mb-4" controlId="job_title">
            <Form.Control
              onChange={(e) => setMessage(e.target.value)}
              value={message}
              autoComplete="off"
              placeholder="comment"
              type="text"
            />
          </Form.Group>
          <Form.Group className="mb-4" controlId="job_title">
            <Button variant="primary" onClick={() => postCourseComment(id, message)}>
              Post
            </Button>
          </Form.Group>
        </Form>        
        {following ? <SavedIcon onClick={()=>handleFollowingClick()} /> 
        : <UnsavedIcon onClick={()=>handleFollowingClick()}/> }
      </div>
      </div>
    </>
  );
};





// career_post_action_by_postid
export { CoursePostDetail };
