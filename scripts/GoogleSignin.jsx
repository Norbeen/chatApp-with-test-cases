
import * as React from 'react';
import { GoogleLogin } from 'react-google-login';
import { Socket } from './Socket';


/*global gapi*/

export class GoogleSignin extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isSignedIn : false,
            user_name : '',
            image_url : ''
        };
    }
    
    render() {
        return (
            
            <div>
      <GoogleLogin
          clientId="641650714654-3nvhsfpcnhgiljvfrhj70f7idk3uv0gi.apps.googleusercontent.co"
          buttonText="Login with Google"
          onSuccess={this.responseGoogle}
          onFailure={this.responseGoogle}
          cookiePolicy={'single_host_origin'}
        />
      </div>
    
        );
    }
}