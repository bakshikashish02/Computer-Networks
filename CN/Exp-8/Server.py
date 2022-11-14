import socket 
s=socket.socket() 
print("socked created")
s.bind(('localhost',9999))
s.listen(3)
print("waiting for the connection") 
while True:

    c,addr=s.accept()
    name=c.recv(1024).decode() 
    print('connected with',addr, name) 
    c.send(bytes('Welcome','utf-8')) 
    c.close()