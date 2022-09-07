import React from 'react';
import { BACKEND_IMAGE_URL, DEFAULT_IMAGE_URL } from 'constants/url';
import { get_url_param_by_id } from 'utils/sdk';
const HeaderPhoto = () => {
  const username = get_url_param_by_id(1);
  return (
    <div style={{ marginLeft: '400px' }}>

        <object          
          data={`${BACKEND_IMAGE_URL}/${username}.png`}
          type="image/png">
          <img            
            alt="default"
            src={DEFAULT_IMAGE_URL}></img>
        </object>      
    </div>
  );
};

export default HeaderPhoto;
