#client
import socket
path="/tmp/server.sock"

host = "127.0.0.1"
port = 5006
with socket.socket(socket.AF_UNIX, socket.SOCK_SEQPACKET) as s:
    s.connect(path)
    
    #give command to server.
    commandstr=input("possible commands: latlong, time, returnstate, ping\n")
    command = commandstr.encode('utf-8')
    s.send(command)
    data=s.recv(1024)
    print(data)