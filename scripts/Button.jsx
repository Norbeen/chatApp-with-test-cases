
import * as React from 'react';
import GoogleLogin  from 'react-google-login';
import { Socket } from './Socket';

/* global gapi */

// Declaring the active user to 0 and setting User signin status to be false

let UserActive = 0;
let UserSignedIn = false;

const responseGoogle = (response) => {
    
    let auth = gapi.auth2.getAuthInstance();
    let user = auth.currentUser.get();
    if (user.isSignedIn()) {
        UserActive += 1
        UserSignedIn = true;
        Socket.emit('google token', {
            'user_token': user.getAuthResponse().id_token
        });
    }
}


// Appending the message( url/non url ), name and image from google to display in the browser

export class Button extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            user_message: ''
        };
        
        this.handleChangeMessage = this.handleChangeMessage.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.sendButton = this.sendButton.bind(this);
    }
    
    
// This will emit the user typed message to the server in python code 

    handleSubmit(event){
        event.preventDefault();
        
        Socket.emit('first_client_message', {
            'user_message': this.state.user_message
        });
// In order to clear the input field after sending the message.
        this.setState({user_message: ''});
        
        console.log('Sent a message to server!',this);
        console.log('User Name:', this.state.user_name);
        console.log('User Message:', this.state.user_message);
    }
    
    handleChangeMessage(event) {
        this.setState({user_message: event.target.value});
        console.log('user_message', event.target.value);
    }
    
// When true this is returned true, that enables the button 

    sendButton() {
        const {user_message} = this.state;
        return user_message.length > 0 && UserSignedIn;
    }
    
    render() {

// client message is the message to be displayed when rendered

        let isEnabled = this.sendButton();
        
        return (
            <div>
                <form className = "enter-chat" onSubmit = {this.handleSubmit}>
                    <div>
                            <GoogleLogin
                                clientId="431399280437-1sl5lk925j49op7h9j0f3a6tmj299ciq.apps.googleusercontent.com"
                                buttonText="Log in with Google"
                                onSuccess={responseGoogle}
                                onFailure={responseGoogle}
                                cookiePolicy={'single_host_origin'}
                                className = "google-login-button"
                            />
                    </div>
                </form>
                
                <form className = "reply-area" onSubmit = {this.handleSubmit}>
                    <div>
                        <textarea className="type-box" cols="100" rows="5" placeholder = " Start your chat" value = {this.state.message} onChange = {this.handleChangeMessage}></textarea>
                    </div>
                    <div>
                        <button disabled = {!isEnabled}> Send </button>
                    </div>
                </form>
            </div>
        );
    }
}