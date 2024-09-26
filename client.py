#client
import socket
path="/tmp/server.sock"

with socket.socket(socket.AF_UNIX, socket.SOCK_SEQPACKET) as s:
    s.connect(path)
    print("Client connected.")
    
    commandstr=input("Possible commands: latlong, time, returnstate, ping\n")
    while commandstr:
        command = commandstr.encode('utf-8')
        s.send(command)
        data=s.recv(1024)
        print(data.decode('utf-8'))
        commandstr=input("possible commands: latlong, time, returnstate, ping\n")
        
print("Client disconnected.")
    
        