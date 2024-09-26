#server
import os
import socket

path="/tmp/server.sock"

if os.path.exists(path):
    os.remove(path)

with socket.socket(socket.AF_UNIX, socket.SOCK_SEQPACKET) as s:
        s.bind(path)
        
        print(f"Starting server on {path}\nWaiting for client.")
        
        s.listen()
        while True:
                conn, addr = s.accept()
                with conn:
                        print("Client connected.")
                        while True:
                                command=conn.recv(1024) #buffsize 1024 bytes
                                command=command.decode("utf-8")
                                data=0
                                if not command:
                                        print("Closing connection.")
                                        break                                        
                                if command == "time":
                                        data=b"12:45 am Friday August 23 2024"
                                elif command == "latlong":
                                        data=b"(53.518291, -113.536530)"
                                elif command == "returnstate":
                                        data=b"return state on"
                                elif command == "ping": 
                                        data=b"ping successful"
                                else:
                                        command="invalid command"
                                        data=b"not a valid command"
                                
                                print(f"Command recieved: {command}.")        
                                conn.send(data)
                                
                        print("Client disconnected.")
                break
        os.remove(path)
        print("Server socket file removed.")