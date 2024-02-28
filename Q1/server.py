import socket
import pickle

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
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

            with open("pickled.txt", "wb") as file:
                file.write(pickle.loads(data))

            message = "file received by the server!"
            client_socket.sendall(message.encode())
        finally:
            client_socket.close()

if __name__ == "__main__":
    run_server()
