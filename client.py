from socket import *
import sys

if len(sys.argv)  < 3 :
    print(f"Usage :{sys.argv[0]} ip port")
    sys.exit(0)

buffer =bytes(1024)
a = True

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((sys.argv[1], int(sys.argv[2])))

file = open("recv.dat", "wb")

print("receiving....")

while a:
    buffer = clientSock.recv(1024)
    file.write(buffer)
    if buffer == b"":
        break
print("receiving complete")
file.close()
