a. What is the theme you’ll be using for project 2?

  -I am using a bot named Jarvis, which is interactive and shows you nearest food places name and yelp website link.

b. How did you incorporate your theme within your project?

  -For this project, I am using flask for backend code, socketio for duplex communication, react (javascript framework for server side),   jsx (javascript and html fusion for rendering html and scripts.js), postgresql(to store user messages), authentication (google login),   for the chatbot I am using yelp API. 

c. What are at least 5 issues you encountered with your project? How did you fix them?

1. First issue was to make sure all the libraries are installed, I had issue installing oauth2 and parse library, I installed them with a little bit of searching.

2. Issue getting data passed to server and client, I used emit and on socketio to do duplex communication with a little documentation study.

3. My code was up and running but I made a mistake in renaming a function, which I later figured out looking at console in chrome and changed the method name.

4. Getting the message to display in textfield, it was hard to incorporate the message with image and the history of the chat, I was finally able to implement postgresql database and conncet to heroku.

5. The deployment of the app in heroku didnt display message, so I had to go over lectures to connect database to heroku.

6. The process of getting google token after authenticating an user was difficult but I was finally able to implement it with going over google developer documentation, also I had to extract name, image which was possible with the documentation.

7. I was using yelp api to get the restaurant near me, it was working fine when I tested it in replit, but while actually implementing in aws, it shows error response doesn't have get command, I am working on that.
Actually I had called responses library from google auth aswell so it was conflicting, when i deleted the conflicting line of code, it worked.

d. What are known problems, if any, with your project?

 -Still in the stage of integrating features, not significant issues.

e. What would you do to tackle these issues?

1. Be ready to read through lines and lines of documentaion, youtube videos won't help, they are not based on aws react.
2. Work early and practice continous integration
