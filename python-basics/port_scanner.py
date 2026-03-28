import socket

target = input("Entrez une IP : ")

print(f"Scan de {target}...")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port ouvert : {port}")

    s.close()
