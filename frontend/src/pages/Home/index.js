// import React, { useEffect } from 'react';
import React from 'react';
import Button from 'react-bootstrap/Button';
import { useDispatch } from 'react-redux';
import { logOut } from 'actions/allActions';
// import { setCoursePost, setCareerPost } from 'actions/allActions';
// import { getCoursePostData, getCareerPostData } from 'utils/crud';

function Home() {
  const dispatch = useDispatch();
  return (
    <div className="home" style={{ marginLeft: '400px' }}>
      <h1>Home</h1>
      <div>
        <Button variant="primary" onClick={() => dispatch(logOut())}>
          Logout button
        </Button>
      </div>
    </div>
  );
}

export default Home;
