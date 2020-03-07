from app import *
global googleImage, googleName
from google.oauth2 import id_token
from google.auth.transport import requests
from app import *

global googleImage 
global googleName 

#***********************  verification of the user signed in with the google *************
@socketio.on('google token')

def google_information(token):
    
    print ("Got an event for GOOGLE TOKEN ID: "+ str(token))
    
    try:
        CLIENT_ID = '431399280437-1sl5lk925j49op7h9j0f3a6tmj299ciq.apps.googleusercontent.com'
        idinfo = id_token.verify_oauth2_token(token['user_token'], requests.Request(), CLIENT_ID)
    
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')
            
        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = idinfo['sub']
        print(idinfo)
        
        # In order to insert on database and send it to client later + making global variable
       
        googleImage = idinfo['picture']
        googleName = idinfo['name']
        
        
        print("************")
        print("Name: "+ idinfo['name'])
        print("Imageurl: "+ idinfo['picture'])
        print("Email: "+ idinfo['email'])
        print("************")
    
    except ValueError:
        print("Invalid token")
