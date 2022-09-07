import React, { useCallback } from 'react';
import { useDispatch } from 'react-redux';
import { GoogleLogin } from 'react-google-login';
import GoogleButton from 'react-google-button';
import { validateTokenAndObtainSession } from './sdk';
import { setLogin } from 'actions/allActions';
import { notifyError } from 'utils/notification';
import 'react-toastify/dist/ReactToastify.css';
import { isErrorClass } from 'utils/sdk';
import 'styles/App.css';
const { REACT_APP_GOOGLE_CLIENT_ID } = process.env;


const Login = () => {
  const dispatch = useDispatch();
  const handleUserInit = useCallback((resp) => {
    if (isErrorClass(resp)) {
      notifyError('Please login with CMU email');
    } else {
      dispatch(setLogin(resp.data));
    }
  }, []);

  const onGoogleLoginSuccess = useCallback((response) => {
    const idToken = response.tokenId;
    const data = {
      email: response.profileObj.email,
      first_name: response.profileObj.givenName,
      last_name: response.profileObj.familyName
    };

    validateTokenAndObtainSession({ data, idToken }).then(handleUserInit).catch(notifyError);
  }, []);
  const googleButtonStyle = {position: 'relative', width: '20rem', height: '3rem', margin: '50% 70%'}
  return (
    <>    
    <div className='login-container'>      
      <GoogleLogin
        render={(renderProps) => <GoogleButton 
        style={googleButtonStyle}
        {...renderProps} 
        />}
        clientId={REACT_APP_GOOGLE_CLIENT_ID}
        buttonText="Sign in with Google"
        onSuccess={onGoogleLoginSuccess}
        onFailure={({ details }) => notifyError(details)}
      />

    </div>
    
    </>
  );
};

export { Login };
