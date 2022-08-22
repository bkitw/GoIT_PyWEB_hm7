import socket


def client():
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    print(f'Servers IP: {host}, port: {port}')
    print('Print "break" to over the connection.')
    message = input('--> ')
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print(f'--- \n Message received from {host}: {data}\n---')
    print('Message delivered. Closing connection.')

    client_socket.close()


if __name__ == '__main__':
    client()