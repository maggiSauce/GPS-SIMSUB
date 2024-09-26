#server
import os
import socket

host = "127.0.0.1"
port = 5006
path="/tmp/server.sock"

with socket.socket(socket.AF_UNIX, socket.SOCK_SEQPACKET) as s:
    s.bind(path)
    
    print(f"Starting server on {host}, port{port}")
    s.listen()
    conn, addr = s.accept()
    with conn:
        command=conn.recv(1024) #buffsize 1024 bytes
        data=0
        if command == b"time":
            data=b"12:45 am Friday August 23 2024"
        elif command == b"latlong":
            data=b"(53.518291, -113.536530)"
        elif command == b"returnstate":
            data=b"return state on"
        elif command == b"ping": 
            data=b"ping successful"
        else:
            data=b"not a valid command"
        conn.send(data)
        conn.close()

os.remove(path)