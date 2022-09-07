import 'styles/App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Login } from 'pages/Login';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ProfilePhoto from 'pages/Photo/ProfilePhoto';
import Profile from 'pages/Profile';
import { ProfileEdit } from 'pages/Profile/ProfileEdit';
import CoursePost from 'pages/CoursePost';
import RelaventPost from 'pages/Course/RelaventPost';
import CoursePostEdit from 'components/Post/PostEdit';
import Error from 'pages/Error';
import SearchCourse from 'pages/Course/SearchCourseTable';
import CreateCoursePost from 'pages/CoursePost/CreateCoursePost';
// import Messages from 'pages/Messages';
import Home from 'pages/Home';
import Navbar from 'components/Navbar/Navbar';
import Settings from 'pages/Settings';
import { CoursePostDetail } from 'components/Post/PostDetail';
import HeaderPhoto from 'pages/Photo/HeaderPhoto';
import { useEffect } from 'react';
import { logOut } from 'actions/allActions';
import { tokenExpire } from './sdk';
import { useSelector } from 'react-redux';
import { useDispatch } from 'react-redux';
import {SavedPost} from 'pages/SavedPost';
import PageNotFound from 'pages/Error/PageNotFound';
const Router = () => {
  const dispatch = useDispatch();

  const isLogin = useSelector((state) => state.isLogin);
  const lastLogin = useSelector((state) => state.last_login);
  // work like cookie, 5 is the minute from last login to current time.
  // If have time, it could be added to users setting avaiability
  useEffect(() => {
    // if (isLogin && tokenExpire(lastLogin, 5)) dispatch(logOut());
    if (isLogin && tokenExpire(lastLogin, 30)) dispatch(logOut());
  }, []);

  return (
    <BrowserRouter>
      {isLogin ? <Navbar /> : null}
      <Routes>
        <Route path="/" element={!isLogin ? <Login /> : <Home />} />        
        <Route path="/profile/:username" element={<Profile />} />
        <Route path="/profile/:username/photo" element={<ProfilePhoto />} />
        <Route path="/profile/:username/header-photo" element={<HeaderPhoto />} />
        <Route path="/coursePost" element={<CoursePost />} />

        <Route path="/coursePost/:id" element={<CoursePostDetail />} />
        <Route path="/coursePost/:id/edit" element={<CoursePostEdit />} />
        <Route path="/course/search" element={<SearchCourse />} />
        <Route path="/course/search/:id" element={<RelaventPost />} />
        <Route path="/coursePost/create-story" element={<CreateCoursePost />} />        
        <Route path="/settings/profile" element={<ProfileEdit />} />
        {/* <Route path="/messages" element={<Messages />} /> */}
        <Route path="/saved" element={<SavedPost />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/error" element={<Error />} />
        <Route path="/pagenotfound" element={<PageNotFound />} />
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
