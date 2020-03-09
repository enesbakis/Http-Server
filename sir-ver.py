import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 80))
server.listen(5)

while True:
    try:
        client, address = server.accept()
        print (client.recv(4096))
        client.send(str.encode("HTTP/1.1 200 OK\n"
         +"Content-Type: text/html\n"
         +"\n" # 
         +"<html><body>Hello World</body></html>\n"))
         
        client.close()
    except KeyboardInterrupt:
        break

server.close()