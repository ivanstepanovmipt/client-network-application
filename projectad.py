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
        serverSocket = socket(AF_INET, SOCK_DGRAM)
        serverSocket.bind(('', int(serverPort)))
        print("The server is ready to receive")
        while 1:
            message, clientAddress = serverSocket.recvfrom(2048)
            modifiedMessage = message.upper()
            serverSocket.sendto(modifiedMessage, clientAddress)
    else :
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        message = input('Input lowercase sentence:')
        clientSocket.sendto(message,(serverName,
        serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage)
        clientSocket.close()
else:
    if client == 1:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName,serverPort))
        sentence = input('Input lowercase sentence:')
        clientSocket.send(sentence)
        modifiedSentence = clientSocket.recv(1024)
        print('From Server:', modifiedSentence)
        clientSocket.close()
    else:
        serverSocket = socket(AF_INET,SOCK_STREAM)
        serverSocket.bind(('',serverPort))
        serverSocket.listen(1)
        print('The server is ready to receive')
        while 1:
            connectionSocket, addr = serverSocket.accept()
            sentence = connectionSocket.recv(1024)
            capitalizedSentence = sentence.upper()
            connectionSocket.send(capitalizedSentence)
            connectionSocket.close()
        
        
    
        
