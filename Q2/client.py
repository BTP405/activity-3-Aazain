import socket
import pickle

def add(x, y):
    return x + y

def run_client(task, worker_nodes):

    for worker in worker_nodes:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(worker)

        try:
            data = pickle.dumps(task)
            client_socket.sendall(data)

            result = client_socket.recv(4096)
            result_data = pickle.loads(result)

            print("Result from", worker, ":", result_data)

        finally:
            client_socket.close()

if __name__ == "__main__":

    workers = [('localhost', 12345), ('localhost', 12346)]
    run_client(add, workers)