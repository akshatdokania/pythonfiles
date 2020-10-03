from socket import *

def createServer():
    serversocket=socket(AF_INET,SOCK_STREAM)
    try:
        serversocket.bind(('localhost',9000))
        serversocket.listen(5)
        while(1):
            (clientsocket,address)=serversocket.accept()
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split('\n')
            if(len(pieces)>1):
                print(pieces[0])
            data = " HTTP/1.1 200 OK\r\n"
            data += "content-type: text/html;charset=utf-8\r\n "
            data += "\r\n"
            data+= "<html><head>yo</head><body> hellu </body></html>"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting Down\n");
    except Exception as exc:
        print("Error");
        print(exc)
    serversocket.close()
print("Accessing http://localhost:9000")
createServer()
