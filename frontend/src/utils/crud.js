/**
 * every function related to CRUD (CREATE, READ, UPDATE, DELETE) would
 * be placed here.
 */
import { get, post, put, redirect } from 'utils/sdk';
import { notifyError } from './notification';
import { isErrorClass, remove, onSuccessOrFail } from 'utils/sdk';

export const getCoursePostData = () => {
  let response = get('course_post').then((resp) => {
    if (isErrorClass(resp)) {
      console.log(resp);
    } else {
      return resp.data;
    }
  });
  return response;
};


export const getFollowedCoursePostData = () => {
  let response = get('follow_course_post').then((resp) => {
    if (isErrorClass(resp)) {
      notifyError(resp.message)
    } else {
      return resp.data;
    }
  });
  return response;
};





export const getCoursePostDataById = (id) => {
  let response = get(`course_post/${id}`).then((resp) => {
    if (isErrorClass(resp)) {
      console.log(resp);
    } else {
      return resp.data.post;
    }
  });
  return response;
};

export const getCoursePostDataWithFilter = (data) => {
  // handle search data a form a valid url for backend coursePost
  const path = `course_post?q=&title=${data['title']}&text=${data['text']}&username=${data['username']}&sort=${data['sort']}`;

  let response = get(path).then((resp) => {
    if (isErrorClass(resp)) {
      console.log(resp);
    } else {
      return resp.data.post;
    }
  });
  return response;
};

export const getCareerPostData = () => {
  let response = post('career_post_search', {}).then((resp) => {
    if (isErrorClass(resp)) {
      console.log(resp);
    } else {
      return resp.data.post;
    }
  });
  return response;
};

export const follow_unfollow_course_post = (id) => {
  post(`course_post/${id}`).then((resp) => {
    console.log(resp);
  });
};



export const postCourseComment = (id, comment) => {
  post(`course_post_comment_by_postid/${id}`, { course_comment_text: comment }).then((resp) => {
    if (isErrorClass(resp)) {
      notifyError(resp.message);
    } else {
      window.location.reload();
    }
  });
};


// type = ENUM ("course_post","career_post")
export const createPost = (type, postContent) => {
  post(type, postContent).then((resp) => onSuccessOrFail(resp, 'You create the post!'));
  setTimeout(
    () => (type === 'course_post' ? redirect('/coursePost') : redirect('/careerPost')),
    1500
  );
};

export const getMentionCourseByCourseId = (id) => {  
  let response = get(`course/${id}`).then((resp) => {
    if (isErrorClass(resp)) {
      redirect('/page')
    } else {
      return resp.data;
    }
  });
  return response;
}

// type could be either course_post or career_post
export const deletePost = async (id, type) => {
  return remove(`${type}/${id}`).then((resp) => onSuccessOrFail(resp, 'deleteOk'));
  // return res
  // let res = await remove(`${type}/${id}`)
  // .then(resp => onSuccessOrFail(resp))
  // return res
  // window.location.reload();
  // redirect(`/${type}`)
  // .then(window.location.reload())
};

// type could be either course_post or career_post
export const editPost = (id, data) => {
  put(`course_post/${id}`, data)
  .then(resp => onSuccessOrFail(resp, 'successfully update'))  
};
