import logging
from socket import *
import argparse
import sys
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
        print(1)
		

def create_parser_argv2():
    parser.add_argument('-f', default = True) 
    return parser


parser.add_argument("sN", type = str)
parser.add_argument("sP", type = str)
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
    _file = namespace.f
print(serverName)
print(serverPort)
print(client)
print(client)
print(protocol)
print(read)
print(file_)
	
	
if protocol == '-u':
    if client == '-s':
        serverSocket = socket(AF_INET, SOCK_DGRAM)  # создаём сокет клиента
        Logging(file_, read, 'opening a socket with a protocol u')
        serverSocket.bind(('', int(serverPort)))   # связываем порт
        while 1:
            message, clientAddress = serverSocket.recvfrom(2048)
            message = str(clientAddress[0]) + ':' + str(clientAddress[1])
            serverSocket.sendto(message.encode(), clientAddress)  # отправляет 
            Logging(file_, read, 'sending a message to a client')
    else:
        clientSocket = socket(AF_INET, SOCK_DGRAM)  # создаём сокет клиента
        Logging(file_, read, 'opening a socket with a protocol u')
        message = input('Input lowercase sentence:')
        clientSocket.sendto(message.encode(), (serverName, int(serverPort))) 
        Logging(file_, read, 'sending a message to a server')
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # ждёт
        Logging(file_, read, 'Receiving a message') 
        print(modifiedMessage.decode())  # выводит полученный ответ
        clientSocket.close()  # завершает свою работу.
        Logging(file_, read, 'Closing the socket')
else:
    if client != '-s':
        clientSocket = socket(AF_INET, SOCK_STREAM)  # создаём сокет клиента
        Logging(file_, read, 'opening a socket with a protocol t')
        ##else:
        ## PrintInFile(read, 'opening a socket')
        clientSocket.connect((serverName, int(serverPort)))
        sentence = input('Input lowercase sentence:')
        clientSocket.send(sentence.encode())  # посылает запрос серверу
        Logging(file_, read, 'sending a message to a server')
        modifiedSentence = clientSocket.recv(1024)  # ждёт ответ сервера;
        Logging(file_, read, 'Receiving a message')
        print('From Server:', modifiedSentence.decode()) 
        clientSocket.close()  # завершает свою работу.
        Logging(file_, read, 'Closing the socket')
    else:
        serverSocket = socket(AF_INET, SOCK_STREAM)  # создаём сокет клиента
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
