import logging
from socket import *
logging.basicConfig(level=logging.DEBUG)


def PrintInFile(name_file, log):
    name_file = read + ".txt"
    file = open("name_file", "w")
    file.write(str(logging.info('opening a socket')))
    file.close()
s = input()
lst = s.split()
serverName = lst[0]
serverPort = lst[1]
protocol = '-t'
read = '-o'
client = 0
i = 2
while i < len(lst):
    if lst[i] == '-s':
        client = 1
    if lst[i] == '-u':
        protocol = '-u'
    if lst[i].find('f') != -1:
        read = lst[len(lst) - 1]
    i = i + 1
if protocol == '-u':
    if client == 1:
        serverSocket = socket(AF_INET, SOCK_DGRAM)  # создаём сокет клиента
        if read == '-o':
            logging.info('opening a socket')
        else:
            PrintInFile(read, 'opening a socket')
        serverSocket.bind(('', int(serverPort)))   # связываем порт
        while 1:
            message, clientAddress = serverSocket.recvfrom(2048)
            message = str(clientAddress[0]) + ':' + str(clientAddress[1])
            serverSocket.sendto(message.encode(), clientAddress)  # отправляет 
            # ответ
            if read == '-o':
                logging.info('Sending a message')
            else:
                PrintInFile(read, 'Sending a message')
    else:
        clientSocket = socket(AF_INET, SOCK_DGRAM)  # создаём сокет клиента
        if read == '-o':
            logging.info('opening a socket')
        else:
            PrintInFile(read, 'opening a socket')
        message = input('Input lowercase sentence:')
        clientSocket.sendto(message.encode(), (serverName, int(serverPort))) 
        if read == '-o':
            logging.info('Sending a message')
        else:
            PrintInFile(read, 'Sending a message')
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # ждёт 
        # ответ сервера;
        if read == '-o':
            logging.info('Receiving a message')
        else:
            PrintInFile(read, 'Receiving a message')
        print(modifiedMessage.decode())  # выводит полученный ответ
        clientSocket.close()  # завершает свою работу.
        if read == '-o':
            logging.info('Closing the socket')
        else:
            PrintInFile(read, 'Closing the socket')
else:
    if client == 0:
        clientSocket = socket(AF_INET, SOCK_STREAM)  # создаём сокет клиента
        if read == '-o':
            logging.info('opening a socket')
        else:
            PrintInFile(read, 'opening a socket')
        clientSocket.connect((serverName, int(serverPort)))
        sentence = input('Input lowercase sentence:')
        clientSocket.send(sentence.encode())  # посылает запрос серверу
        if read == '-o':
            logging.info('Sending a message')
        else:
            PrintInFile(read, 'Sending a message')
        modifiedSentence = clientSocket.recv(1024)  # ждёт ответ сервера;
        if read == '-o':
            logging.info('Receiving a message')
        else:
            PrintInFile(read, 'Receiving a message')
        print('From Server:', modifiedSentence.decode()) 
        clientSocket.close()  # завершает свою работу.
        if read == '-o':
            logging.info('Closing the socket')
        else:
            PrintInFile(read, 'Closing the socket')
    else:
        serverSocket = socket(AF_INET, SOCK_STREAM)  # создаём сокет клиента
        if read == '-o':
            logging.info('opening a socket')
        else:
            PrintInFile(read, 'opening a socket')
        serverSocket.bind(('', int(serverPort)))
        serverSocket.listen(1)
        while 1:
            connectionSocket, addr = serverSocket.accept()
            sentence = connectionSocket.recv(1024)
            capitalizedSentence = str(addr[0]) + ':' + str(addr[1])
            connectionSocket.send(capitalizedSentence.encode())
            if read == '-o':
                logging.info('Sending a message')
            else:
                PrintInFile(read, 'Sending a message')
            connectionSocket.close()
