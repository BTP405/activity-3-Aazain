import socket
import threading
import pickle

HOST = 'localhost'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

clients = []
lock = threading.Lock()


def handle_client(client, address):
    print(f"{address} connected.")

    with lock:
        clients.append((client, address))

    connected = True
    while connected:
        try:
            data = client.recv(1024)
            if data:
                message = pickle.loads(data)
                print(f"Received message from {address}: {message}")
                broadcast(message)

        except Exception as error:
            print(f"Error occured while handling client {address}: {error}")

            with lock:
                clients.remove((client, address))
            
            print(f"{address} disconnected.")
            client.close()
            break


def broadcast(message):
    with lock:
        for client, address in clients:
            try:
                client.send(pickle.dumps(message))
            except:
                clients.remove((client, address))


def start():
    server.listen()
    print(f"Server is listening on {HOST}:{PORT}")
    while True:
        client, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, address))
        thread.start()


print("Server is starting...")
start()
