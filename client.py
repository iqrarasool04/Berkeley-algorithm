import socket
import time

#function to synchronize
def synchronize_time(server_address):

    #socket creation and connection
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    #sending request to server
    T_0 = time.time()
    client_socket.send(str(T_0).encode())

    #receiving time from server
    T_1 = float(client_socket.recv(1024).decode())

    #calculating time difference
    time_difference = T_1 - T_0

    print(f"Received Time from Slave Node: {T_1}")
    print(f"Time Difference: {time_difference}")

    #closing socket
    client_socket.close()

server_address = ('localhost', 12345)
for i in range(6):
    print(f"Client {i+1}:")
    synchronize_time(server_address)
