import socket

def input_matrix():
    matrix = []
    print("Introduceți elementele matricei:")
    for i in range(2):
        row = []
        for j in range(2):
            element = float(input(f"Element [{i + 1}][{j + 1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def main():
    server_ip = '127.0.0.1'  # Adresa IP a serverului
    server_port = 12345  # Portul serverului
    server_address = (server_ip, server_port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    while True:
        matrix = input_matrix()
        option = int(input("Alege o opțiune (1 - Dublare, 2 - Determinant, 3 - Urmă): "))

        matrix_data = str(matrix)
        client_socket.send(matrix_data.encode())

        option_data = str(option)
        client_socket.send(option_data.encode())

        response = client_socket.recv(1024).decode()
        print("Răspuns de la server:", response)

        repeat = input("Doriți să repetați acțiunea? (Da/Nu): ")
        if repeat.lower() != "da":
            break

    client_socket.close()

if __name__ == "__main__":
    main()
