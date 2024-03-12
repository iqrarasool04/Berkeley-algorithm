import socket
import time

#function for server functionality
def start_server(server_address):

    #socket creation and connection
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)

    print("Clock Server is listening...")

    slave_times = []

    while True:
        #accepting client connection and receiving request
        client_socket, client_address = server_socket.accept()
        T_0 = float(client_socket.recv(1024).decode())
        
        #sending server's time to client
        T_SERVER = time.time()
        client_socket.send(str(T_SERVER).encode())

        #calculating time difference
        time_difference = T_SERVER - T_0

        #adding time difference to list
        slave_times.append(time_difference)

        #closing socket
        client_socket.close()

        #breaking loop after 6 clients
        if len(slave_times) == 6:
            break

    #average time difference
    average_time_difference = sum(slave_times) / len(slave_times)

    #synchronized time
    synchronized_times = [T_SERVER - time_difference + average_time_difference for time_difference in slave_times]

    #printing synchronized time
    for i, sync_time in enumerate(synchronized_times):
        print(f"Synchronized Time for Client {i+1}: {sync_time}")

server_address = ('localhost', 12345)
start_server(server_address)
