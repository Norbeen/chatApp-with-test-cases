
import * as React from 'react';
import GoogleLogin  from 'react-google-login';
import { Socket } from './Socket';

/* global gapi */


let UserActive = 0;
let UserSignedIn = false;

const responseGoogle = (response) => {
    console.log("Hey, I am from Button.js")
    console.log("*************");
    
    let auth = gapi.auth2.getAuthInstance();
    let user = auth.currentUser.get();
    if (user.isSignedIn()) {
        UserActive += 1
        UserSignedIn = true;
        console.log("Is user signed in:",UserSignedIn)
        console.log("google token:  " + user.getAuthResponse().id_token);
        Socket.emit('google token', {
            'user_token': user.getAuthResponse().id_token
        });
    }
}

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
    
    handleSubmit(event){
        event.preventDefault();
        //  *** user-message and user_name is sent from client to server ***
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
    
    sendButton() 
    
    {
    if (this.state.user_message != null && UserSignedIn){
      return true;  
    }
    else{
        return false;
    }
    }
    
    render() {
        
        let client_message = this.state.message;
        let send_message= this.handleSubmit;
        let receive_message =this.handleChangeMessage;
        
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
                
                <form className = "reply-area" onSubmit = {send_message}>
                    <div>
                        <textarea className="type-box" cols="50" rows="2" placeholder = " Start your chat" value = {client_message} onChange = {receive_message}></textarea>
                    </div>
                    <div>
                        <button enabled = {this.sendButton()}> Send </button>
                    </div>
                </form>
            </div>
        );
    }
}