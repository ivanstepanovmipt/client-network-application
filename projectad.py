import logging
from socket import *
logging.basicConfig(level=logging.DEBUG)
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
if protocol == '-t':
    if client == 1:
        serverSocket = socket(AF_INET, SOCK_DGRAM) #создаём сокет клиента
        serverSocket.bind(('', int(serverPort))) #связываем порт, определённого номера с сокетом сервера
        while 1:
            message, clientAddress = serverSocket.recvfrom(2048)
            modifiedMessage = serverName + ' : ' + serverPort
            serverSocket.sendto(modifiedMessage, clientAddress) #при получении запроса отправляет ответ, содержащий ip адрес и порт клиента.
    else :
        clientSocket = socket(AF_INET, SOCK_DGRAM) #создаём сокет клиента
        if read == '-o':
            logging.info('opening a socket')
        else:
            file = open("read.txt", "w")
            file.write(logging.info('opening a socket'))
            file.close()
        message = input('Input lowercase sentence:')
        clientSocket.sendto(message,(serverName,serverPort)) #посылает запрос серверу по указанному адресу;
        if read == '-o':
            logging.info('Sending a message')
        else:
            file = open("read.txt", "w")
            file.write(logging.info('Sending a message'))
            file.close()
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #ждёт ответ сервера;
        if read == '-o':
            logging.info('Receiving a message')
        else:
            file = open("read.txt", "w")
            file.write(logging.info('Receiving a message'))
            file.close()
        print(modifiedMessage) #выводит полученный ответ
        clientSocket.close() #завершает свою работу.
        if read == '-o':
            logging.info('Closing the socket')
        else:
            file = open("read.txt", "w")
            file.write(logging.info('Closing the socket'))
            file.close()
        
else:
    if client == 0:
        clientSocket = socket(AF_INET, SOCK_STREAM) #создаём сокет клиента
        if read == '-o':
            logging.info('opening a socket')
        else:
            file = open("read.txt", "w")
            file.write(logging.info('opening a socket'))
            file.close()
        clientSocket.connect((serverName,serverPort))
        sentence = input('Input lowercase sentence:')
        clientSocket.send(sentence) #посылает запрос серверу по указанному адресу;
        if read == '-o':
            logging.info('Sending a message')
        else:
            file = open("read.txt", "w")
            file.write(logging.info('Sending a message'))
            file.close()
        modifiedSentence = clientSocket.recv(1024) #ждёт ответ сервера;
        if read == '-o':
            logging.info('Receiving a message')
        else:
            file = open("read.txt", "w")
            file.write(logging.info('Receiving a message'))
            file.close()
        print('From Server:', modifiedSentence) #выводит полученный отве
        clientSocket.close() #завершает свою работу.
        if read == '-o':
            logging.info('Closing the socket')
        else:
            file = open("read.txt", "w")
            file.write(logging.info('Closing the socket'))
            file.close()
    else:
        serverSocket = socket(AF_INET,SOCK_STREAM) #создаём сокет клиента
        serverSocket.bind(('',serverPort))
        serverSocket.listen(1)
        while 1:
            connectionSocket, addr = serverSocket.accept()
            sentence = connectionSocket.recv(1024)
            capitalizedSentence = serverName + ' : ' + serverPort
            connectionSocket.send(capitalizedSentence)
            connectionSocket.close()
        
        
