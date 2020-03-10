import os, flask, flask_socketio, flask_sqlalchemy, random
from requests import *
import models
# Importing library for parsing and validation of URIs (RFC 3986)
from rfc3987 import parse
from google.oauth2 import id_token
import google.auth.transport.requests
from google.auth.transport import requests
from ChatBot import yelp_api
from ValidateUrl import validateUrl
request = google.auth.transport.requests.Request()


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
    
googleImage = ""
googleName = ""  

#  #***********************  verification of the user signed in with the google *****************
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
        
def Bot(name, message):
  
    if message == "!! say something":
        message = "Hello, welcome to the chatroom. I am Jarvis, here to help you!"
    elif message == "!! about":
         message = "Hi, I am Jarvis. I was designed by Nabin in Maryland for this project."
    elif message == "!! help":
        message = "Commands: '!! about','!! say something','!! source','!! developer'"
    elif message == "!! source":
        message = "To find the source code of this web-app, visit the github.com/norbeen tab at the top the page."
    elif message == "!! developer":
        message = "I was designed by Nabin for his project. Want to know more about him? Visit github.com/norbeen."
    elif message == "!! Jarvis food near me" or message == "!! Jarvis food":
          message = yelp_api()
          name = "Jarvis"
    else:
        message= "Sorry! I am unable to answer this question. Type '!! help' to see the lists of commands."
    return name, message


# name= "nabin"
# message= "!! Jarvis food"
# print(Bot(name, message)) 
        
#   #***************** Getting message after authentication as user submits the message ***********     

@socketio.on('first_client_message')
def on_received_Message(data):
  
    grabbedMessage  = data['user_message']
  
    # Checking response for the bot.
    if grabbedMessage[:2]=="!!":
        
        global googleName
        showName = Bot(googleName, grabbedMessage )[0]
        showMessage = Bot(googleName, grabbedMessage )[1]
        print("#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(showName)
        print(showMessage)
    else:
        showName = googleName
        showMessage = grabbedMessage
        

    message = models.chatMessage(showName,showMessage,googleImage)
    models.db.session.add(message)
    models.db.session.commit()
    chatLog = [] 
    
#     # Retrieving the data from database
    database_messages = models.chatMessage.query.all()
    
    
    print("Stored Messages:", database_messages)
    
    for i in database_messages:
        
        name = i.Uname
        message = i.Umessage
        image = i.Uimage
        
# # # #   #****************************** Validating if the message is URL or NO url ***********************
        url = validateUrl(message)[0]
        non_url = validateUrl(message)[1]
    

# # # #   #Appending the google name, url/url message and the image
  
        
        display_list = [name, url, non_url, image]
        chatLog.append(display_list)


    socketio.emit('push to server', {'database_list': chatLog});
    
# #   #****************************** This ends here ***************************************************  
  
  
        
if __name__ =='__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )