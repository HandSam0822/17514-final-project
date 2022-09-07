import {
  LOGIN,
  LOGOUT,
  SET_COURSE_POST,
  SET_CAREER_POST,
  EDIT_PROFILE
} from '../constants/actionTypes';
const initState = {
  name: '',
  isLogin: false
};

const reducers = (state = initState, action) => {
  switch (action.type) {
    case LOGIN:
      return {
        ...state,
        isLogin: true,
        id: action.payload.id,
        token: action.payload.token,
        first_name: action.payload.first_name,
        last_name: action.payload.last_name,
        username: action.payload.username,
        last_login: action.payload.last_login,
        date_joined: action.payload.date_joined,
        email: action.payload.email,
        location: action.payload.location,
        bio: action.payload.bio,
        user_point: action.payload.user_point
      };
    case LOGOUT:
      return {
        isLogin: false
      };
    case SET_COURSE_POST:
      return {
        ...state,
        coursePost: action.payload
      };

    case SET_CAREER_POST:
      return {
        ...state,
        careerPost: action.payload
      };
    case EDIT_PROFILE:
      console.log(action.payload);
      return {
        ...state,
        username: action.payload.username,
        bio: action.payload.bio,
        location: action.payload.location
      };

    default:
      return state;
  }
};

export default reducers;
