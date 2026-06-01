import socket

host = "127.0.0.1"
port = 3535

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host, port))

while True:
    mensagem = input("Digite uma mensagem para o servidor: ")

    if mensagem == "sair":
        break

    cliente.send(mensagem.encode())
    resposta = cliente.recv(1024).decode()
    print(f"Resposta do servidor: {resposta}")
