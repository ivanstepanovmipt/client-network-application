import logging
from socket import *
import argparse
import sys
from __future__ import print_function
parser = argparse.ArgumentParser()


def Logging(name_file, logging_mode, log):
    if logging_mode == '-o':
        logging.basicConfig(level=logging.DEBUG)
        logging.info(str(log))
    else:
        logging.basicConfig(filename=name_file, level=logging.INFO)
        logging.basicConfig(
            filename=name_file,
            filemode='w',
            format='%(name)s - %(levelname)s - %(message)s'
        )
        logging.info(str(log))


def create_parser_argv2():
    parser.add_argument('-f', default=True)
    return parser


def UDP_Server(serverName, serverPort, read):
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    Logging(file_, read, 'opening a socket with a protocol u')
    serverSocket.bind(('', int(serverPort)))
    while 1:
        message, clientAddress = serverSocket.recvfrom(2048)
        message = str(clientAddress[0]) + ':' + str(clientAddress[1])
        serverSocket.sendto(message.encode(), clientAddress)
        Logging(file_, read, 'sending a message to a client')


def UDP_Client(serverName, serverPort, read):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    Logging(file_, read, 'opening a socket with a protocol u')
    message = 'hello'
    clientSocket.sendto(message.encode(), (serverName, int(serverPort)))
    Logging(file_, read, 'sending a message to a server')
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    Logging(file_, read, 'Receiving a message')
    print(modifiedMessage.decode())
    clientSocket.close()
    Logging(file_, read, 'Closing the socket')


def TSP_Client(serverName, serverPort, read):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    Logging(file_, read, 'opening a socket with a protocol t')
    clientSocket.connect((serverName, int(serverPort)))
    sentence = 'hello'
    clientSocket.send(sentence.encode())
    Logging(file_, read, 'sending a message to a server')
    modifiedSentence = clientSocket.recv(1024)
    Logging(file_, read, 'Receiving a message')
    print('From Server:', modifiedSentence.decode())
    clientSocket.close()
    Logging(file_, read, 'Closing the socket')


def TSP_Server(serverName, serverPort, read):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    Logging(file_, read, 'opening a socket with a protocol t')
    serverSocket.bind(('', int(serverPort)))
    serverSocket.listen(1)
    while 1:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024)
        capitalizedSentence = str(addr[0]) + ':' + str(addr[1])
        connectionSocket.send(capitalizedSentence.encode())
        Logging(file_, read, 'sending a message to a client')
        connectionSocket.close()


parser.add_argument("sN", type=str)
parser.add_argument("sP", type=str)
parser.add_argument("-s", action="store_true")
parser.add_argument("-u", action="store_true")
parser.add_argument("-t", action="store_true")
parser.add_argument("-o", action="store_true")
parser1 = create_parser_argv2()
namespace = parser1.parse_args(sys.argv[1:])
args = parser.parse_args()

file_ = 'aaa'
serverName = args.sN
serverPort = args.sP
client = '-c'
protocol = '-t'
read = '-o'
if args.s:
    client = '-s'
if args.u and args.t:
    logging.info('error')
    sys.exit()
if args.u:
    protocol = '-u'
file_ = str(namespace.f)
print(file_)
if file_ == "True":
    read = '-o'
if file_ != "True":
    read = '-f'
    file_ = namespace.f
if protocol == '-u':
    if client == '-s':
        UDP_Server(serverName, serverPort, read)
    else:
        UDP_Client(serverName, serverPort, read)
else:
    if client != '-s':
        TSP_Client(serverName, serverPort, read)
    else:
        TSP_Server(serverName, serverPort, read)

