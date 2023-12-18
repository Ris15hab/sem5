import socket

def mpm():
    host = '127.0.0.1'
    port = 6000
    s = socket.socket()
    s.bind((host,port))
    s.listen(1)
    print("Waiting for connection...")
    c, addr = s.accept()
    print("Connection Established!")
    print(f"Client Address: {addr}")
    while True:
        try:
            print()
            data = c.recv(1024)
            msg = data.decode('ascii')
            print(f"Client: {msg}")
            print()
            msg = input("Enter a message: ")
            msg = msg.encode('ascii')
            c.send(msg)
        except KeyboardInterrupt:
            print()
            print("Connection terminated...")
            break

mpm()