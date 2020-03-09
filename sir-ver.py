import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 80))
server.listen(5)
print ("{}:{} dinleniyor...".format(*server.getsockname()))

while True:
    try:
        client, address = server.accept()
        print ("{}:{} bağlandı".format(*address))
        print (client.recv(4096))
        file = open("index.html","r",encoding= "utf-8")
        client.send(str.encode("HTTP/1.1 200 OK\n"
         +"Content-Type: text/html\n"
         +"Http-Server: sir-ver v0.1\n"
         +"\n"
         +file.read()
         +"\n"))
         
        client.close()
    except KeyboardInterrupt:
        break

server.close()