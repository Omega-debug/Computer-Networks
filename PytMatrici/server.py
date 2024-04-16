import socket

def double_matrix(matrix):
    return [[2 * matrix[i][j] for j in range(2)] for i in range(2)]

def calculate_determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def calculate_trace(matrix):
    return matrix[0][0] + matrix[1][1]

def main():
    server_ip = '127.0.0.1'  # Adresa IP a serverului
    server_port = 12345  # Portul serverului
    server_address = (server_ip, server_port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print("Serverul este pornit și așteaptă conexiuni...")

    while True:
        client_socket, client_address = server_socket.accept()

        data = client_socket.recv(1024).decode()
        matrix = eval(data)  # Se așteaptă date sub forma unei liste Python

        data = client_socket.recv(1024).decode()
        option = int(data)

        if option == 1:
            result = double_matrix(matrix)
        elif option == 2:
            result = calculate_determinant(matrix)
        elif option == 3:
            result = calculate_trace(matrix)
        else:
            result = "Opțiune invalidă"

        client_socket.send(str(result).encode())
        client_socket.close()

if __name__ == "__main__":
    main()
