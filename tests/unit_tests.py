import unittest
import ChatBot
from ChatBot import *

class ChatBotResponseTest(unittest.TestCase):
    def test_say_something(self):
        response = ChatBot.Bot("nabin", "!! say something")
        self.assertEqual(response[1], "Hello, welcome to the chatroom. I am Jarvis, here to help you!")
        
    def test_about(self):
        response = ChatBot.Bot("nabin","!! about")
        self.assertEqual(response[1], "Hi, I am Jarvis. I was designed by Nabin in Maryland for this project.")
        
    def test_help(self):
        response = ChatBot.Bot("nabin","!! help")
        self.assertEqual(response[1], "Commands: '!! about','!! say something','!! source','!! developer', '!! Jarvis food near me', '!! Jarvis food','!! Make me happy', '!! jokes', '!! humor'")
        
    def test_source(self):
        response = ChatBot.Bot("nabin","!! source")
        self.assertEqual(response[1], "To find the source code of this web-app, visit the github.com/norbeen tab at the top the page.")
        
    def test_developer(self):
        response = ChatBot.Bot("nabin","!! developer")
        self.assertEqual(response[1], "I was designed by Nabin for his project. Want to know more about him? Visit github.com/norbeen.")

    
    def test_not_valid(self):
        response = ChatBot.Bot("nabin", "!! not valid")
        self.assertEqual(response[1],"Sorry! I am unable to answer this question. Type '!! help' to see the lists of commands.")
        
    def test_JarvisfoodNear(self):
        response = ChatBot.Bot("nabin","!! Jarvis food near me")
        self.assertEqual(response[1], resName + " " + resUrl)
        
    def test_foodNear(self):
        response = ChatBot.Bot("nabin","!! humor")
        self.assertEqual(response[1],  jokeList[randNum])
        
    def test_jokes(self):
        response = ChatBot.Bot("nabin","!! jokes")
        self.assertEqual(response[1], jokeList[randNum])
        
    def test_error(self):
        response = ChatBot.Bot("nabin","!! Make me happy")
        self.assertEqual(response[1], jokeList[randNum])

if __name__ == '__main__':
    unittest.main()