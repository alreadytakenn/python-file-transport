from socket import *
import sys

if len(sys.argv)  < 3 :
    print(f"Usage :{sys.argv[0]} file port")
    sys.exit(0)

file = open(sys.argv[1], "rb")

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', int(sys.argv[2])))
serverSock.listen()

clientSock, addr = serverSock.accept()
buffer = bytes(file.read())
print("sending....")
clientSock.send(buffer)

print("sending complete")

file.close()
