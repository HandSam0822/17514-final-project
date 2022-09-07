import React from 'react';
import saved from 'assets/icon/saved.png'; // relative path to image
import unsaved from 'assets/icon/unsaved.png'; 
import search from 'assets/icon/search.png'; 
import message from 'assets/icon/message.png'; 
import profile from 'assets/icon/profile.png'; 
import course from 'assets/icon/course.png'; 
import home from 'assets/icon/home.png'; 
import setting from 'assets/icon/setting.png'; 
import archive from 'assets/icon/archive.png'; 
import writing from 'assets/icon/writing.png'; 
import 'styles/icon.css';

export const SavedIcon = (props) => {
  return <img className="saved" onClick={()=>props.onClick()} alt="saved" src={saved}></img>;
};

export const UnsavedIcon = (props) => {
  return <img className="unsaved" onClick={()=>props.onClick()} alt="unsaved" src={unsaved}></img>;
};

export const SearchIcon = () => {
  return <img className="search" alt="search" src={search}></img>;
};

export const MessageIcon = () => {
  return <img className="navbar-icon" alt="message" src={message}></img>;
};

export const ProfileIcon = () => {
  return <img className="navbar-icon" alt="message" src={profile}></img>;
};

export const CourseIcon = () => {
  return <img className="navbar-icon" alt="course" src={course}></img>;
};

export const HomeIcon = () => {
  return <img className="navbar-icon" alt="home" src={home}></img>;
};

export const SettingIcon = () => {
  return <img className="navbar-icon" alt="setting" src={setting}></img>;
};


export const ArchiveIcon = () => {
  return <img className="navbar-icon" alt="archive" src={archive}></img>;
};

export const WritingIcon = () => {
  return <img className="navbar-icon" alt="writing" src={writing}></img>;
};
