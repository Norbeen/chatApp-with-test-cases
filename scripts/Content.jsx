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
        
        let final_messages = this.state.messages;
      
      return (
            <div>
            
 <section className="chat-app">
                    <div className="container">
                        <h4 className="welcome-text">Chat bot</h4>
                        <div className="message-log">
                            <div className="message-block">
                                <ul>
                                    <li className = "chatbot">
                                        <h5 className="user-name">Bot</h5>
                                        <p className="user-message">chatbot</p>
                                    </li>
                                    { final_messages.map( name_message =>
                                    <li key = {name_message[0].id} className = "message-with-image">
                                        <img src={name_message[3]} alt = "User Image" className = "user-image"></img>
                                        <div>
                                            <h5 className="user-name"> {name_message[0]}</h5>
                                            {(name_message[1].length > 0) && <a className="user-message" href = {name_message[1]} target="_blank">Link attached.</a>}
                                            {(name_message[2].length > 0) && <p className="user-message"> {name_message[2]} </p>}
                                            
                                        </div>
                                    </li> )}
                                </ul>
                            </div>
                        </div>
                        
                        <div>
                            <Button />
                        </div>
                        
                    </div>
                </section>
            </div>
        );
    }
}

