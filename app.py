import os, flask, flask_socketio, flask_sqlalchemy, random
from requests import *
import models
# Importing library for parsing and validation of URIs (RFC 3986)
from rfc3987 import parse
from google.oauth2 import id_token
from google.auth.transport import requests
from ChatBot import *
from ValidateUrl import validateUrl


googleImage = ""
googleName = ""



app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)

@app.route('/')
def hello():
    return flask.render_template('index.html')
    
@socketio.on('connect')
def on_connect():
    print('Someone connected!')

@socketio.on('disconnect')
def on_disconnect():
    print('Someone disconnected!')
    

 #***********************  verification of the user signed in with the google *****************
@socketio.on('google token')
def google_information(token):
    
    print ("Got an event for GOOGLE TOKEN ID: "+ str(token['user_token']))
    
    try:
        CLIENT_ID = '431399280437-1sl5lk925j49op7h9j0f3a6tmj299ciq.apps.googleusercontent.com'
        idinfo = id_token.verify_oauth2_token(token['user_token'], requests.Request(), CLIENT_ID)
    
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
            
        #**************** After verification getting the user id.     ************************
        userid = idinfo['sub']
        print(idinfo)
        
        # ***************** Declaring global variable for name and image extracted from google ********
       
        global googleImage
        googleImage= idinfo['picture']
        
        global googleName
        googleName = idinfo['name']
    
    except ValueError:
        print("Invalid token")
        
        
        
  #***************** Getting message after authentication as user submits the message ***********     

@socketio.on('first_client_message')

def received_Message(data):
    print ("Got an event for new message with data: "+ str(data))
    # server_received_name = data['user_name']
    grabMessage = data['user_message']
    print(grabmessage)
    
    
    # Checking response for the bot.
    if grabMessage[:2] == "!!":
        
        received_Message= Bot(googleName, received_Message)[0]
        received_Name = Bot(googleName, received_Message)[1]

    message = models.Message(googleName, received_Message, googleImage)
    models.db.session.add(message)
    models.db.session.commit()
    
    print("Record inserted successfully")
    
    # Retrieving the data from database
    database_messages = models.Message.query.all()
    display_list = []
    print("Stored Messages:", database_messages)
    
    for i in database_messages:
        
        name = s.user_name
        message = s.user_message
        image = s.user_image
        
  #****************************** Validating if the message is URL or NO url ***********************
        url = validateUrl(message)[0]
        non_url = validateUrl(message)[1]
        # ********
  
  #Appending the google name, url/url message and the image
  
        # chat_list = [name, message, image]
        chat_list = [name, url, non_url, image]
        new_list.append(chat_list)
        
    print("New List: ", display_list)

    # *** Lists of username and message sent from server to every client ***
    socketio.emit('push to server', {'database_list': display_list});
    
  #****************************** This ends here ***************************************************  
  
  

    


        
        
if __name__ =='__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )