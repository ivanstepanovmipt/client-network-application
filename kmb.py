"""
Client-server application
"""
from __future__ import print_function
import logging
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
import argparse
import sys
# pylint: disable=E1101


def logg(name_file, logging_mode, log):
    """Logging to file or command line."""
    if logging_mode == '-o':
        logging.info(str(log))
    else:
        logging.basicConfig(
            filename=name_file,
            filemode='w',
            format='%(name)s - %(levelname)s - %(message)s'
        )
        logging.info(str(log))


def create_parser_argv2():
    """nothing."""
    PARSER.add_argument('-f', default=True)
    return PARSER


def udp_server(port_server, r):
    """Starting the server in UDP mode."""
    server_socket = socket(AF_INET, SOCK_DGRAM)
    logg(FILE_, r, 'opening a socket with a protocol u')
    server_socket.bind(('', int(port_server)))
    while 1:
        try:
            message, client_address = server_socket.recvfrom(2048)
            message = str(client_address[0]) + ':' + str(client_address[1])
            server_socket.sendto(message.encode(), client_address)
            logg(FILE_, r, 'sending a message to a client')
        except KeyboardInterrupt:
            logg(FILE_, r, 'the server is shutting down')
            sys.exit(0)


def udp_client(name_server, port_server, r):
    """Starting the client in UDP mode."""
    client_socket = socket(AF_INET, SOCK_DGRAM)
    logg(FILE_, r, 'opening a socket with a protocol u')
    message = 'hello'
    client_socket.sendto(message.encode(), (name_server, int(port_server)))
    logg(FILE_, r, 'sending a message to a server')
    modified_message, server_address = client_socket.recvfrom(2048)
    logg(FILE_, r, 'Receiving a message')
    print(modified_message.decode())
    client_socket.close()
    logg(FILE_, r, 'Closing the socket')


def tcp_client(name_server, port_server, r):
    """Starting the client in TSP mode."""
    client_socket = socket(AF_INET, SOCK_STREAM)
    logg(FILE_, r, 'opening a socket with a protocol t')
    client_socket.connect((name_server, int(port_server)))
    sentence = 'hello'
    client_socket.send(sentence.encode())
    logg(FILE_, r, 'sending a message to a server')
    modified_sentence = client_socket.recv(1024)
    logg(FILE_, r, 'Receiving a message')
    print('From Server:', modified_sentence.decode())
    client_socket.close()
    logg(FILE_, r, 'Closing the socket')


def tcp_server(port_server, r):
    """Starting the server in TSP mode."""
    server_socket = socket(AF_INET, SOCK_STREAM)
    logg(FILE_, r, 'opening a socket with a protocol t')
    server_socket.bind(('', int(port_server)))
    server_socket.listen(1)
    while 1:
        try:
            connection_socket, addr = server_socket.accept()
            capitalized_sentence = str(addr[0]) + ':' + str(addr[1])
            connection_socket.send(capitalized_sentence.encode())
            logg(FILE_, r, 'sending a message to a client')
            connection_socket.close()
        except KeyboardInterrupt:
            logg(FILE_, r, 'the server is shutting down')
            sys.exit(0)
PARSER = argparse.ArgumentParser()
PARSER.add_argument("sN", type=str)
PARSER.add_argument("sP", type=str)
PARSER.add_argument("-s", action="store_true")
COMMAND_GROUP = PARSER.add_mutually_exclusive_group()
COMMAND_GROUP.add_argument('-u', help='TCP Protocol', action='store_true')
COMMAND_GROUP.add_argument('-t', help='UDP Protocol', action='store_true')
PARSER.add_argument("-o", action="store_true")
PARSER_1 = create_parser_argv2()
NAMESPACE = PARSER_1.parse_args(sys.argv[1:])
ARGS = PARSER.parse_args()

FILE_, SERVER_NAME, SERVERPORT = 'aaa', ARGS.sN, ARGS.sP
CLIENT, PROTOCOL, READ = '-c', '-t', '-o'
if ARGS.s:
    CLIENT = '-s'
if ARGS.u:
    PROTOCOL = '-u'
FILE_ = str(NAMESPACE.f)
if FILE_ == "True":
    READ = '-o'
    logging.basicConfig(level=logging.DEBUG)
if FILE_ != "True":
    READ = '-f'
    FILE_ = NAMESPACE.f
    logging.basicConfig(filename=FILE_, level=logging.INFO)
if PROTOCOL == '-u':
    if CLIENT == '-s':
        udp_server(SERVERPORT, READ)
    else:
        udp_client(SERVER_NAME, SERVERPORT, READ)
else:
    if CLIENT != '-s':
        tcp_client(SERVER_NAME, SERVERPORT, READ)
    else:
        tcp_server(SERVERPORT, READ)
