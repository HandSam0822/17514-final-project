import {
  LOGIN,
  LOGOUT,
  SET_COURSE_POST,
  SET_CAREER_POST,
  EDIT_PROFILE
} from 'constants/actionTypes';

export const setLogin = (user_data) => async (dispatch) => {
  try {
    dispatch({ type: LOGIN, payload: user_data });
  } catch (error) {
    console.log(error.message);
  }
};

export const setCoursePost = (coursePost) => async (dispatch) => {
  try {
    dispatch({ type: SET_COURSE_POST, payload: coursePost });
  } catch (error) {
    console.log(error);
  }
};

export const setCareerPost = (careerPost) => async (dispatch) => {
  try {
    dispatch({ type: SET_CAREER_POST, payload: careerPost });
  } catch (error) {
    console.log(error);
  }
};

export const logOut = () => async (dispatch) => {
  try {
    dispatch({ type: LOGOUT, payload: '' });
  } catch (error) {
    console.log(error.message);
  }
};

export const editProfile = (newProfile) => async (dispatch) => {
  try {
    dispatch({ type: EDIT_PROFILE, payload: newProfile });
  } catch (error) {
    console.log(error);
  }
};
