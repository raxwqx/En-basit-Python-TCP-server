import socket

HOST = "0.0.0.0"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(5)

print(f"[*] TCP Server başlatıldı: {HOST}:{PORT}")

while True:
    client, address = server.accept()

    print(f"[+] Bağlantı: {address[0]}:{address[1]}")

    client.sendall(b"Hello from Python TCP Server!\n")

    client.close()
