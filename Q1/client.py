import socket
import pickle

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    try:
        file_path = "q1.txt"
        with open(file_path, "rb") as file:
            file_data = file.read()
            pickle_data = pickle.dumps(file_data)
            client_socket.sendall(pickle_data)

        data = client_socket.recv(1024)
        print("Received acknowledgment:", data.decode())

    finally:
        client_socket.close()

if __name__ == "__main__":
    run_client()