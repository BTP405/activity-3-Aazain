import socket
import threading
import pickle

HOST = 'localhost'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def receive():
    while True:
        try:
            message = client.recv(1024)
            if message:
                print(pickle.loads(message))
        except:
            print("Error")
            client.close()
            break


def send():
    while True:
        message = input()
        try:
            client.send(pickle.dumps(message)) 
        except:
            print("Error")
            client.close()
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
