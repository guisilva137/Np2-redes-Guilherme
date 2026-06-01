import socket

host = "127.0.0.1"
port = 3535

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print("Servidor ouvindo na porta 3535...")

while True:
    cliente, endereco = server.accept()
    print(f"Cliente conectado: {endereco}")

    while True:
        mensagem = cliente.recv(1024).decode()
        print(f"Mensagem recebida: {mensagem}")

        if mensagem == "sair":
            break

        resposta = input("Digite uma resposta para o cliente: ")
        cliente.send(resposta.encode())

    cliente.close()