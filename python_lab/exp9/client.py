import socket

def mpm():
    host = '127.0.0.1'
    port = 6000
    s = socket.socket()
    s.connect((host,port))
    print("Connection established...")
    while True:
        try:
            print()
            msg = input("Enter a message: ")
            msg = msg.encode('ascii')
            s.send(msg)
            print()
            msg = s.recv(1024)
            msg = msg.decode('ascii')
            print(f"Client: {msg}")
        except KeyboardInterrupt:
            print()
            print("Connection Terminated!")
            s.send("Connection from Client terminated!".encode('ascii'))
            break

mpm()