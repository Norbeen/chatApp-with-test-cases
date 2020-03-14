import app
import unittest

class socketio_test(unittest.TestCase):
    
    def test_server_connecting(self):
        client =app.socketio.test_client(app.app)
        
        response = client.get_received()
        
        self.assertEqual(len(response), 1)
        from_server_connect = response[0]
        self.assertEqual(from_server_connect['name'], "hey client")
        
        data = from_server_connect['args'][0]
        self.assertEqual(data['connect message'], "hey server")
        
    def test_server_disconnecting(self):
        
        client = app.socketio.test_client(app.app)
        client.emit('disconnect', {'I am disconnecting': 'disconnected'})
        response = client.get_received()
        self.assertEqual(len(response), 2)
        
        from_server = response[1]
        self.assertEqual(from_server['name'], 'disconnecting')
        
        data = from_server['args'][0]
        self.assertEqual(data['disconnect status'], 'disconnected')

    def test_server_relays_message(self):
        client = app.socketio.test_client(app.app)
        client.emit('new message', {'my message': 'I am Nabin'})
        response = client.get_received()
        self.assertEqual(len(response), 2)
        
        from_server = response[1]
        self.assertEqual(from_server['name'], 'got your message')
        
        data = from_server['args'][0]
        self.assertEqual(data['your message'], 'I am Nabin')
        
    
    def test_google_token(self):
        client = app.socketio.test_client(app.app)
        client.emit('google-token', {'token': 'this is token'})
        response = client.get_received()
        self.assertEqual(len(response), 2)
        
        from_server = response[1]
        self.assertEqual(from_server['name'], 'google token')
        
        data = from_server['args'][0]
        self.assertEqual(data['token'], 'this is token')
        
        
    def test_server_test_message(self):
        client = app.socketio.test_client(app.app)
        client.emit('test message', {'my test message': 'just testing'})
        response = client.get_received()
        self.assertEqual(len(response), 2)
        
        from_server = response[1]
        self.assertEqual(from_server['name'], 'got test message')
        
        data = from_server['args'][0]
        self.assertEqual(data['my test message'], 'just testing')
       

if __name__ == '__main__':
    unittest.main()