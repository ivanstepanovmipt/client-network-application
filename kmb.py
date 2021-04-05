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
    parser.add_argument('-f', default=True)
    return parser


def udp_server(port_server, r):
    """Starting the server in UDP mode."""
    server_socket = socket(AF_INET, SOCK_DGRAM)
    logg(file_, r, 'opening a socket with a protocol u')
    server_socket.bind(('', int(port_server)))
    while 1:
        try:
            message, client_address = server_socket.recvfrom(2048)
            message = str(client_address[0]) + ':' + str(client_address[1])
            server_socket.sendto(message.encode(), client_address)
            logg(file_, r, 'sending a message to a client')
        except KeyboardInterrupt:
            logg(file_, r, 'the server is shutting down')
            sys.exit(0)


def udp_client(name_server, port_server, r):
    """Starting the client in UDP mode."""
    client_socket = socket(AF_INET, SOCK_DGRAM)
    logg(file_, r, 'opening a socket with a protocol u')
    message = 'hello'
    client_socket.sendto(message.encode(), (name_server, int(port_server)))
    logg(file_, r, 'sending a message to a server')
    modified_message, _ = client_socket.recvfrom(2048)
    logg(file_, r, 'Receiving a message')
    print(modified_message.decode())
    client_socket.close()
    logg(file_, r, 'Closing the socket')


def tcp_client(name_server, port_server, r):
    """Starting the client in TSP mode."""
    client_socket = socket(AF_INET, SOCK_STREAM)
    logg(file_, r, 'opening a socket with a protocol t')
    client_socket.connect((name_server, int(port_server)))
    sentence = 'hello'
    client_socket.send(sentence.encode())
    logg(file_, r, 'sending a message to a server')
    modified_sentence = client_socket.recv(1024)
    logg(file_, r, 'Receiving a message')
    print('From Server:', modified_sentence.decode())
    client_socket.close()
    logg(file_, r, 'Closing the socket')


def tcp_server(port_server, r):
    """Starting the server in TSP mode."""
    server_socket = socket(AF_INET, SOCK_STREAM)
    logg(file_, r, 'opening a socket with a protocol t')
    server_socket.bind(('', int(port_server)))
    server_socket.listen(1)
    while 1:
        try:
            connection_socket, addr = server_socket.accept()
            capitalized_sentence = str(addr[0]) + ':' + str(addr[1])
            connection_socket.send(capitalized_sentence.encode())
            logg(file_, r, 'sending a message to a client')
            connection_socket.close()
        except KeyboardInterrupt:
            logg(file_, r, 'the server is shutting down')
            sys.exit(0)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sN", type=str)
    parser.add_argument("sP", type=str)
    parser.add_argument("-s", action="store_true")
    command_group = parser.add_mutually_exclusive_group()
    command_group.add_argument('-u', help='TCP Protocol', action='store_true')
    command_group.add_argument('-t', help='UDP Protocol', action='store_true')
    parser.add_argument("-o", action="store_true")
    parser_1 = create_parser_argv2()
    namespace = parser_1.parse_args(sys.argv[1:])
    args = parser.parse_args()
    
    file_, server_name, serverport = 'aaa', args.sN, args.sP
    client, protocol, read = '-c', '-t', '-o'
    if args.s:
        client = '-s'
    if args.u:
        protocol = '-u'
    file_ = str(namespace.f)
    if file_ == "True":
        read = '-o'
        logging.basicConfig(level=logging.DEBUG)
    if file_ != "True":
        read = '-f'
        file_ = namespace.f
        logging.basicConfig(filename=file_, level=logging.INFO)
    if protocol == '-u':
        if client == '-s':
            udp_server(serverport, read)
        else:
            udp_client(server_name, serverport, read)
    else:
        if client != '-s':
            tcp_client(server_name, serverport, read)
        else:
            tcp_server(serverport, read)
