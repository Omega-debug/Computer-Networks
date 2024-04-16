import socket
import random
import math

server_ip = "127.0.0.1"  # IP-ul pe care serverul va asculta
server_port = 12345  # Portul pe care serverul va asculta

# Creează un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Leagă socket-ul la o adresă IP și port
sock.bind((server_ip, server_port))

def primulet(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

while True:
    print("Așteptăm pentru a primi date...")
    data, address = sock.recvfrom(1024)
    data = data.decode('utf-8')

    if data == "optiunea1":
        raspuns = str(random.randint(1, 100))
    elif data.startswith("optiunea2"):
        numar = int(data.split(":")[1])
        raspuns = str(numar * 2)
    elif data.startswith("optiunea3"):
        numar = int(data.split(":")[1])
        if numar % 2 == 0:
            raspuns = "Numărul este par"
        else:
            raspuns = "Numărul este impar"
    elif data.startswith("optiunea4"):
        numar = int(data.split(":")[1])
        if primulet(numar):
            raspuns = "Numărul este prim"
        else:
            raspuns = "Numărul nu este prim"
    else:
        raspuns = "Opțiune invalidă"

    print(f"Am primit: {data}, Trimit: {raspuns}")
    sock.sendto(raspuns.encode('utf-8'), address)
