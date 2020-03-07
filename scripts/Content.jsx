import * as React from 'react';
import { Button } from './Button';
import { Socket } from './Socket';



export class Content extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            'messages': []
        };
        this.componentDidMount = this.componentDidMount.bind(this);
    }
    
    componentDidMount(){
        
        Socket.on('push to server', (data) => {this.setState({'messages': data['database_list']})});
        console.log('Lets see:', this.state);
        console.log(this.state.messages)
    }
    
    render() {
        
        let display_message = this.state.messages;
      return (
            <div>
            
            
            
            
<section className="msger">
  <header className="msger-header">
    <div className="msger-header-title">
      <i className="fas fa-comment-alt"></i> Nabin's Chatbot
    </div>
    <div className="msger-header-options">
      <span><i className="fas fa-cog"></i></span>
    </div>
  </header>

  <main className="msger-chat">
    <div className="m sg left-msg">
      <div className="msg-bubble">
        <div className="msg-info">
          <div className="msg-info-name">BOT</div>
          <div className="msg-info-time">12:45</div>
        </div>

       
                                <ul>
                                    <li className = "msg-text">
                                         <div className="msg-text">
                                         Hi, welcome to the chat, Go ahead and send me a message. 😄
                                        </div>
                                   
                                    </li>
                                    { display_message.map( name_message =>
                                    <li key = {name_message[0].id} className = "message-with-image">
                                        <img src={name_message[3]} alt = "User Image" className = "user-image"></img>
                                        <div>
                                            <h5 className="user-name"> {name_message[0]}</h5>
                                            {(name_message[1].length > 0) && <a className="msg-text" href = {name_message[1]} target="_blank">Link attached.</a>}
                                            {(name_message[2].length > 0) && <p className="msg-text"> {name_message[2]} </p>}
                                            
                                        </div>
                                    </li> )}
                                </ul>
                            </div>
                        </div>
                        
                        <div>
                            <Button />
                        </div>
                      </main>  
                </section>
             </div>
        );
    }
}