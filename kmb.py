import logging
from socket import *
import argparse
import sys
logging.basicConfig(level=logging.DEBUG)
parser = argparse.ArgumentParser()


def PrintInFile(name_file, log):
    name_file = read + ".txt"
    file = open("name_file", "w")
    file.write(str(logging.info('opening a socket')))
    file.close()

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
        ##if read == '-o':
        logging.info('opening a socket')
        ##else:
            ##PrintInFile(read, 'opening a socket')
        serverSocket.bind(('', int(serverPort)))   # связываем порт
        while 1:
            message, clientAddress = serverSocket.recvfrom(2048)
            message = str(clientAddress[0]) + ':' + str(clientAddress[1])
            serverSocket.sendto(message.encode(), clientAddress)  # отправляет 
            # ответ
            ##if read == '-o':
            logging.info('Sending a message')
            ##else:
               ## PrintInFile(read, 'Sending a message')
    else:
        clientSocket = socket(AF_INET, SOCK_DGRAM)  # создаём сокет клиента
        ##if read == '-o':
        logging.info('opening a socket')
        ##else:
         ##   PrintInFile(read, 'opening a socket')
        message = input('Input lowercase sentence:')
        clientSocket.sendto(message.encode(), (serverName, int(serverPort))) 
        ##if read == '-o':
        logging.info('Sending a message')
        ##else:
           ## PrintInFile(read, 'Sending a message')
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # ждёт 
        # ответ сервера;
        ##if read == '-o':
        logging.info('Receiving a message')
        ##else:
            ##PrintInFile(read, 'Receiving a message')
        print(modifiedMessage.decode())  # выводит полученный ответ
        clientSocket.close()  # завершает свою работу.
        ##if read == '-o':
        logging.info('Closing the socket')
        ##else:
            ##PrintInFile(read, 'Closing the socket')
else:
    if client != '-s':
        clientSocket = socket(AF_INET, SOCK_STREAM)  # создаём сокет клиента
        ##if read == '-o':
        logging.info('opening a socket')
        ##else:
        ## PrintInFile(read, 'opening a socket')
        clientSocket.connect((serverName, int(serverPort)))
        sentence = input('Input lowercase sentence:')
        clientSocket.send(sentence.encode())  # посылает запрос серверу
        ##if read == '-o':
        logging.info('Sending a message')
        ##else:
            ##PrintInFile(read, 'Sending a message')
        modifiedSentence = clientSocket.recv(1024)  # ждёт ответ сервера;
        ##if read == '-o':
        logging.info('Receiving a message')
        ##else:
           ## PrintInFile(read, 'Receiving a message')
        print('From Server:', modifiedSentence.decode()) 
        clientSocket.close()  # завершает свою работу.
        ##if read == '-o':
        logging.info('Closing the socket')
        ##else:
           ## PrintInFile(read, 'Closing the socket')
    else:
        serverSocket = socket(AF_INET, SOCK_STREAM)  # создаём сокет клиента
        ##if read == '-o':
        logging.info('opening a socket')
        ##else:
            ##PrintInFile(read, 'opening a socket')
        serverSocket.bind(('', int(serverPort)))
        serverSocket.listen(1)
        while 1:
            connectionSocket, addr = serverSocket.accept()
            sentence = connectionSocket.recv(1024)
            capitalizedSentence = str(addr[0]) + ':' + str(addr[1])
            connectionSocket.send(capitalizedSentence.encode())
            ##if read == '-o':
            logging.info('Sending a message')
            ##else:
               ## PrintInFile(read, 'Sending a message')
            connectionSocket.close()
