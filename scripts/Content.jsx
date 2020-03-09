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
            </div>
                                <ul>
                                    <li className = "msg-text">
                                         <div className="msg-text">
                                         Hi, welcome to the chat, Go ahead and send me a message. 😄
                                        </div>
                                   
                                    </li>
                                    { display_message.map( show_message =>
                                    <li key = {show_message[0].id} className = "message-with-image">
                                        <img src={show_message[3]} alt = "User Image" className = "user-image"></img>
                                        <div>
                                            <h5 className="user-name"> {show_message[0]}</h5>
                                            {(show_message[1].length > 0) && <a className="msg-text" href = {show_message[1]} target="_blank">Link attached.</a>}
                                            {(show_message[2].length > 0) && <p className="msg-text"> {show_message[2]} </p>}
                                            
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

