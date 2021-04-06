"""
Client-server application
"""
from __future__ import print_function
import logging
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
import argparse
import sys
# pylint: disable=E1101


def udp_server(port_server):
    """Starting the server in UDP mode."""
    server_socket = socket(AF_INET, SOCK_DGRAM)
    logging.info('opening a socket with a protocol u')
    server_socket.bind(('', int(port_server)))
    while 1:
        try:
            message, client_address = server_socket.recvfrom(2048)
            message = str(client_address[0]) + ':' + str(client_address[1])
            server_socket.sendto(message.encode(), client_address)
            logging.info('sending a message to a client')
        except KeyboardInterrupt:
            logging.info('the server is shutting down')
            sys.exit(0)


def udp_client(name_server, port_server):
    """Starting the client in UDP mode."""
    client_socket = socket(AF_INET, SOCK_DGRAM)
    logging.info('opening a socket with a protocol u')
    message = 'hello'
    client_socket.sendto(message.encode(), (name_server, int(port_server)))
    logging.info('sending a message to a server')
    modified_message, _ = client_socket.recvfrom(2048)
    logging.info('Receiving a message')
    print(modified_message.decode())
    client_socket.close()
    logging.info('Closing the socket')


def tcp_client(name_server, port_server):
    """Starting the client in TSP mode."""
    client_socket = socket(AF_INET, SOCK_STREAM)
    logging.info('opening a socket with a protocol t')
    client_socket.connect((name_server, int(port_server)))
    sentence = 'hello'
    client_socket.send(sentence.encode())
    logging.info('sending a message to a server')
    modified_sentence = client_socket.recv(1024)
    logging.info('Receiving a message')
    print('From Server:', modified_sentence.decode())
    client_socket.close()
    logging.info('Closing the socket')


def tcp_server(port_server):
    """Starting the server in TSP mode."""
    server_socket = socket(AF_INET, SOCK_STREAM)
    logging.info('opening a socket with a protocol t')
    server_socket.bind(('', int(port_server)))
    server_socket.listen(1)
    while 1:
        try:
            connection_socket, addr = server_socket.accept()
            capitalized_sentence = str(addr[0]) + ':' + str(addr[1])
            connection_socket.send(capitalized_sentence.encode())
            logging.info('sending a message to a client')
            connection_socket.close()
        except KeyboardInterrupt:
            logging.info('the server is shutting down')
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
    parser.add_argument("-f", dest='file_', type=str)
    args = parser.parse_args()
    server_name, serverport = args.sN, args.sP
    if args.file_:
        logging.basicConfig(filename=args.file_, level=logging.INFO)
    else:
        logging.basicConfig(level=logging.INFO)
    if args.u:
        if args.s:
            udp_server(serverport)
        else:
            udp_client(server_name, serverport)
    else:
        if args.s:
            tcp_server(serverport)
        else:
            tcp_client(server_name, serverport)
