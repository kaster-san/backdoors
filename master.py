import socket
print("master")
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="127.0.0.1"
port=8080
ss.bind((host,port))
ss.listen(5)

print("waiting for connection ...")
conn,addr=ss.accept()
print("client connected successfully")
while True:
    command=input('command >>')
    if command == 'cwd':
        conn.send(command.encode('ascii'))
        print('command sent, waiting for execution ...')
        files=conn.recv(5000)
        files=files.decode('ascii')
        print('the working directory is : ',str(files))

    elif command == 'ls':
        conn.send(command.encode('ascii'))
        user=input('enter the costum directory: ')
        conn.send(user.encode('ascii'))
        file=conn.recv(5000)
        file=file.decode('ascii')
        print('result: ',file)

    elif command == 'download':
        conn.send(command.encode('ascii'))
        path=input(str('enter the path of the file: '))
        conn.send(path.encode('ascii'))
        file=conn.recv(5000)
        filename=input(str('enter the file name: '))
        new = open(filename,'wb')
        new.write(file)
        new.close()
        print(filename,' has been downloaded and saved!')

    elif command == 'close':
        conn.send(command.encode('ascii'))


    else:
        print('command not recognised')
