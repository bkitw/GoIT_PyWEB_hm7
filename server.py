import socket


def main():
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    port = 5000
    print(f'Server\'s IP: {host}, port: {port}\nWaiting for client.')
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    data = conn.recv(100).decode()

    if not data:
        print('Got nothing.')
    print('Client send a message:')
    print(f'|{data}|')

    conn.send('OK'.encode())

    conn.close()



if __name__ == '__main__':
    main()