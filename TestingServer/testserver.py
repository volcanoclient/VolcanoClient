import socket
import sys

class TestServer:
    HOST = 'localhost' # Symbolic name meaning all available interfaces
    PORT = 8888 # Arbitrary non-privileged port

    def __init__(self):
        try:
            self.activeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket Created")
        except socket.error as msg:
            print('Failed to bind : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()

    def start(self):
        try:
            self.activeSocket.bind((self.HOST, self.PORT))
            print("Socket Bound")
            self.activeSocket.listen(10) # more than ten simultanious connections will be rejected
            print("Socket Listening")
        except socket.error as msg:
            print('Failed to start : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit()

    def process(self):
        # now keep talking with the client
        while 1:
            # wait to accept a connection - blocking call
            conn, addr = self.activeSocket.accept()
            print('Connected with ' + addr[0] + ':' + str(addr[1]))
            data = conn.recv(1024)
            reply = 'OK...' + data
            if not data:
                break

            conn.sendall(reply)