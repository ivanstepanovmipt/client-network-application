"""
Client-server application
"""
from __future__ import print_function
import logging
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, SOCK_RAW, IPPROTO_RAW, IPPROTO_IP, IP_HDRINCL, IPPROTO_TCP, inet_aton, htons
import argparse
import sys
import struct
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
    client_socket = socket(AF_INET, SOCK_RAW, IPPROTO_RAW)
    logging.info('opening a socket with a protocol t')
    client_socket.connect((name_server, int(port_server)))
    client_socket.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
    client_socket.send(IP() + TCP() + 'hello'.encode())
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

def IP():
    version = 4
    ihl = 5
    TOS = 0
    Tlen = 0
    ID = 0
    Flag = 0
    Fragment = 0
    TTL = 64
    Proto = IPPROTO_TCP
    ip_checksum = 0
    SIP = inet_aton("127.0.0.1")
    DIP = inet_aton("127.0.0.1")
    ver_ihl = (version << 4) + ihl
    f_f = (Flag << 13) + Fragment
    ip_hdr =  struct.pack("!BBHHHBBH4s4s", ver_ihl,TOS,Tlen,ID,f_f,TTL,Proto,ip_checksum,SIP,DIP)
    return ip_hdr
    
    
def TCP():
    tcp_source = 13000
    tcp_dest = 13000
    tcp_seq = 0
    tcp_ack_seq = 0
    tcp_doff = 5
    tcp_fin = 0
    tcp_syn = 1
    tcp_rst = 0
    tcp_psh = 0
    tcp_ack = 0
    tcp_urg = 0
    tcp_window = 0
    tcp_check = 0
    tcp_urg_ptr = 0
    tcp_offset_res = (tcp_doff << 4) + 0
    tcp_flags = tcp_fin + (tcp_syn << 1) + (tcp_rst << 2) + (tcp_psh <<3) + (tcp_ack << 4) + (tcp_urg << 5)
    tcp_header = struct.pack('!HHLLBBHHH' , tcp_source, tcp_dest, tcp_seq, tcp_ack_seq, tcp_offset_res, tcp_flags,  tcp_window, tcp_check, tcp_urg_ptr)
    return tcp_header
    
    
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
