import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';
import 'styles/Navbar.css';
import { ArchiveIcon, MessageIcon, ProfileIcon, CourseIcon, HomeIcon, SettingIcon, WritingIcon } from 'components/Icon';

function Navbar() {
  const username = useSelector((state) => state.username);
  return (
    <>
      <nav className="nav-menu">
        <ul className="nav-menu-items">
          <li key="0" className="nav-text">
            <Link to="/">
              {' '}
              <HomeIcon />
              <span> Home</span>{' '}
            </Link>
          </li>
          <li key="1" className="nav-text">
            <Link to="/coursePost">
              <CourseIcon />
              <span> Course Post</span>{' '}
            </Link>
          </li>

          <li key="2" className="nav-text">
            <Link to="/course/search">
              <CourseIcon />
              <span> Course </span>{' '}
            </Link>
          </li>

        
          <li key="3" className="nav-text">
            <Link to={`/profile/${username}`}>
              {' '}
              <ProfileIcon />
              <span> Profile</span>{' '}
            </Link>
          </li>
{/* 
          <li key="4" className="nav-text">
            <Link to="/messages">
              <MessageIcon />
              <span> Messages </span>{' '}
            </Link>
          </li> */}

          <li key="5" className="nav-text">
            <Link to="/saved">
              {' '}
              <ArchiveIcon />
              <span> Following </span>{' '}
            </Link>
          </li>

          {/* <li key="6" className="nav-text">
            <Link to="/settings">
              {' '}
              <SettingIcon />
              <span> Settings </span>{' '}
            </Link>
          </li> */}

          <li key="7" className="nav-text">
            <Link to="/coursePost/create-story">
              {' '}
              <WritingIcon />
              <span> Create post </span>{' '}
            </Link>
          </li>
        </ul>
      </nav>
    </>
  );
}

export default Navbar;
