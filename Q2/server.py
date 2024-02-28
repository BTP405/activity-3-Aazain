import socket
import pickle
from client import add

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345) #change port for each worker node
    server_socket.bind(server_address)
    server_socket.listen(1)

    print("Server is listening for incoming connections...")

    while True:
        client_socket, client_address = server_socket.accept()

        try:
            print("Connected to:", client_address)
            data = client_socket.recv(1024)
            if not data:
                break

            task = pickle.loads(data)
            result = task(2, 22)
            
            client_socket.sendall(pickle.dumps(result))
        finally:
            client_socket.close()

if __name__ == "__main__":
    run_server()
