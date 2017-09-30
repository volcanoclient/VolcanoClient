import socket

GOOGLE_DETAILS = {'host': 'www.google.com',
                  'port': 80}

TEST_DETAILS = {'host': 'localhost',
                'port': 8888}

class CustomSocket:
    remote_ip = None
    hostDetails = None
    activeSocket = None
    isConnected = False

    def __init__(self, hostDetails):
        try:
            # create an AF_INET (IPV4), STREAM socket (TCP)
            newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.hostDetails = hostDetails
            self.activeSocket = newSocket
        except socket.errno as e:
            print("unable to create socket: {}".format(str(e)))
        except socket.gaierror as e:
            print("unable to connect to host: {}".format(str(e)))

    def connect(self):
        try:
            self.remote_ip = socket.gethostbyname(self.hostDetails['host'])
            self.activeSocket.connect((self.remote_ip, self.hostDetails['port']))
            self.isConnected = True
        except socket.errno as e:
            print("unable to create socket: {}".format(str(e)))
        except socket.gaierror as e:
            print("unable to connect to host: {}".format(str(e)))

    def disconnect(self):
        try:
            self.activeSocket.close()
            self.isConnected = False
        except socket.errno as e:
            print("unable to create socket: {}".format(str(e)))
        except socket.gaierror as e:
            print("unable to connect to host: {}".format(str(e)))

    def status(self):
        return 'connected to {} as {}'.format(self.hostDetails['host'], self.remote_ip) if self.isConnected else 'disconnected'

    def send(self):
        # Send some data to remote server
        message = "GET / HTTP/1.1\r\n\r\n"
        try:
            # Set the whole string
            self.activeSocket.sendall(message)
        except socket.error:
            print('Unable to send : {}'.format(message))

    def retrieve(self):
        try:
            # Set the whole string
            dataChunk = self.activeSocket.recv(4096)
        except socket.error:
            print('Unable to retrieve')

        return dataChunk