from customsocket import CustomSocket, TEST_DETAILS, GOOGLE_DETAILS

class Messenger:
    socket = None

    def connect(self):
        if not self.socket:
            self.socket = CustomSocket(GOOGLE_DETAILS)
        self.socket.connect()

    def disconnect(self):
        self.socket.disconnect()

    def status(self):
        if self.socket:
            return self.socket.status()

        return 'Not connected'

    def getMainPage(self):
        if self.socket.isConnected:
            self.socket.send()
            return self.socket.retrieve()