import socket

GOOGLE_DETAILS = {'host': 'www.google.com',
                  'port': 80}

TEST_DETAILS = {'host': 'localhost',
                'port': 8888}

FLIST_UNENCRYPTED_TEST = {'host': 'chat.f-list.net',
                            'port': 8722}

FLIST_UNENCRYPTED_LIVE = {'host': 'chat.f-list.net',
                            'port': 9722}

FLIST_ENCRYPTED_TEST = {'host': 'chat.f-list.net',
                            'port': 8799}

FLIST_ENCRYPTED_LIVE = {'host': 'chat.f-list.net',
                            'port': 9799}

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

    def send(self, data):
        # Send some data to remote server
        try:
            # Set the whole string
            self.activeSocket.sendall(data)
        except socket.error:
            print('Unable to send : {}'.format(data))

    MSGLEN = 0

    def retrieve(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < self.MSGLEN:
            chunk = self.activeSocket.recv(4)
            if chunk == '':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return ''.join(chunks)