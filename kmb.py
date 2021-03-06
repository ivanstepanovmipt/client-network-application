import logging
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
import argparse
import sys
parser = argparse.ArgumentParser()


def Logging(name_file, logging_mode, log):
    """Logging to file or command line."""
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
    """nothing."""
    parser.add_argument('-f', default=True)
    return parser


def UDP_Server(Portserver, r):
    """Starting the server in UDP mode."""
    server_socket = socket(AF_INET, SOCK_DGRAM)
    Logging(file_, r, 'opening a socket with a protocol u')
    server_socket.bind(('', int(Portserver)))
    while 1:
        message, client_address = server_socket.recvfrom(2048)
        message = str(client_address[0]) + ':' + str(client_address[1])
        server_socket.sendto(message.encode(), client_address)
        Logging(file_, r, 'sending a message to a client')


def UDP_Client(Nameserver, Portserver, r):
    """Starting the client in UDP mode."""
    client_socket = socket(AF_INET, SOCK_DGRAM)
    Logging(file_, r, 'opening a socket with a protocol u')
    message = 'hello'
    client_socket.sendto(message.encode(), (Nameserver, int(Portserver)))
    Logging(file_, r, 'sending a message to a server')
    modified_message, server_address = client_socket.recvfrom(2048)
    Logging(file_, r, 'Receiving a message')
    print(modified_message.decode())
    client_socket.close()
    Logging(file_, r, 'Closing the socket')


def TSP_Client(Nameserver, Portserver, r):
    """Starting the client in TSP mode."""
    client_socket = socket(AF_INET, SOCK_STREAM)
    Logging(file_, r, 'opening a socket with a protocol t')
    client_socket.connect((Nameserver, int(Portserver)))
    sentence = 'hello'
    client_socket.send(sentence.encode())
    Logging(file_, r, 'sending a message to a server')
    modified_sentence = client_socket.recv(1024)
    Logging(file_, r, 'Receiving a message')
    print('From Server:', modified_sentence.decode())
    client_socket.close()
    Logging(file_, r, 'Closing the socket')


def TSP_Server(Portserver, r):
    """Starting the server in TSP mode."""
    server_socket = socket(AF_INET, SOCK_STREAM)
    Logging(file_, r, 'opening a socket with a protocol t')
    server_socket.bind(('', int(Portserver)))
    server_socket.listen(1)
    while 1:
        connection_socket, addr = server_socket.accept()
        sentence = connection_socket.recv(1024)
        capitalized_sentence = str(addr[0]) + ':' + str(addr[1])
        connection_socket.send(capitalized_sentence.encode())
        Logging(file_, r, 'sending a message to a client')
        connection_socket.close()


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
    logging.basicConfig(level=logging.DEBUG)
    logging.info('error')
    sys.exit()
if args.u:
    protocol = '-u'
file_ = str(namespace.f)
if file_ == "True":
    read = '-o'
if file_ != "True":
    read = '-f'
    file_ = namespace.f
if protocol == '-u':
    if client == '-s':
        UDP_Server(serverPort, read)
    else:
        UDP_Client(serverName, serverPort, read)
else:
    if client != '-s':
        TSP_Client(serverName, serverPort, read)
    else:
        TSP_Server(serverPort, read)
