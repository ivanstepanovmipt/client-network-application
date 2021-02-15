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
print(protocol)
print(read)
print(client)
        
        
    
        
