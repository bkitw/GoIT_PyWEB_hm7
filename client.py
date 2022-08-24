import socket


def client():
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    try:
        message = input('Write a message to server or send "break" to cut the connection:\n---> ')

        while message.lower().strip() != 'break':
            print('Now wait for message from server...')
            try:
                client_socket.send(message.encode())
                data = client_socket.recv(1024).decode()
                if data == 'break':
                    print('--- Connection with server lost. ---')
                    break
            except ConnectionAbortedError:
                print('--- Connection with server lost. ---')
                break

            print(f'Message received from {host}/server:\n|{data}|')
            message = input('--> ')
        print('--- Connection dismissed. ---')
        client_socket.close()
    except KeyboardInterrupt:
        print('--- Connection interrupted manually! ---')
        client_socket.close()


if __name__ == '__main__':
    client()
