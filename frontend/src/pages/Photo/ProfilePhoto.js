import React from 'react';
import { BACKEND_IMAGE_URL } from 'constants/url';
import { get_url_param_by_id } from 'utils/sdk';

const ProfilePhoto = () => {
  const username = get_url_param_by_id(1);
  return (
    <div style={{ marginLeft: '400px' }}>
      <img alt="" style={{width: "400px", height: "400px"}} src={`${BACKEND_IMAGE_URL}/${username}.png`}></img>
    </div>
  );
};

export default ProfilePhoto;
