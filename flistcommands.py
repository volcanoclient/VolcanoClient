
import constants as c
import json

def ping(socket):
    socket.send(c.IDENTIFIER['ping'])
    return socket.receive()

def getCommand(identifier, **kwargs):
    return '{} {}'.format(identifier, str(kwargs))