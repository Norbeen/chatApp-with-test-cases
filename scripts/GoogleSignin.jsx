
import * as React from 'react';
import { GoogleLogin } from 'react-google-login';
import { Socket } from './Socket';


/*global gapi*/

const responseGoogle = (response) => {
    console.log("Hey, I am from Button.js")
    console.log("*************");
    
    let auth = gapi.auth2.getAuthInstance();
    let user = auth.currentUser.get();
    if (user.isSignedIn()) {
        Socket.emit('google token', {
            'user_token': user.getAuthResponse().id_token
        });
    }
}


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
          clientId="431399280437-1sl5lk925j49op7h9j0f3a6tmj299ciq.apps.googleusercontent.com"
          buttonText="Login with Google"
          onSuccess={this.responseGoogle}
          onFailure={this.responseGoogle}
          cookiePolicy={'single_host_origin'}
        />
      </div>
    
        );
    }
}