import unittest
import ChatBot

class ChatBotResponseTest(unittest.TestCase):
    def test_say_something(self):
        response = ChatBot.Bot("nabin", "!! say something")
        self.assertEqual(response[1], "Hello, welcome to the chatroom. I am Jarvis, here to help you!")
        
    def test_about(self):
        response = ChatBot.Bot("nabin","!! about")
        self.assertEqual(response[1], "Hi, I am Jarvis. I was designed by Nabin in Maryland for this project.")
        
    def test_list_command(self):
        response = ChatBot.Bot("nabin","!! help")
        self.assertEqual(response[1], "Commands: '!! about','!! say something','!! source','!! developer'")
        
    def test_source(self):
        response = ChatBot.Bot("nabin","!! source")
        self.assertEqual(response[1], "To find the source code of this web-app, visit the github.com/norbeen tab at the top the page.")
        
    def test_developer(self):
        response = ChatBot.Bot("nabin","!! developer")
        self.assertEqual(response[1], "I was designed by Nabin for his project. Want to know more about him? Visit github.com/norbeen.")
        
    # def test_add_command4(self):
    #     response = ChatBot.Bot("nabin","!! Jarvis food near me")
    #     self.assertEqual(response[1], "Oops! I didn't recognize your command :(")
    
    def test_not_valid(self):
        response = ChatBot.Bot("nabin", "!! not valid")
        self.assertEqual(response[1],"Sorry! I am unable to answer this question. Type '!! help' to see the lists of commands.")

if __name__ == '__main__':
    unittest.main()