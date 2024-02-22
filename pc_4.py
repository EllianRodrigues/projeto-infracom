from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

def receive_messages(socket):
    while True:
        message, address = socket.recvfrom(2048)
        print(f"\nMensagem recebida de {address}: {message.decode()}")

def send_message(socket, address):
    while True:
        target_pc = input("Insira o numero do pc que deseja enviar (1 or 3): ")
        if target_pc == '1':
            message = input("Insira a mensagem para PC1: ")
            socket.sendto(message.encode(), pc1_address)
        elif target_pc == '3':
            message = input("Insira a mensagem para PC3: ")
            socket.sendto(message.encode(), pc3_address)
        else:
            print("Número inválido. Apenas entre 1 or 3.")

# Configuração do socket do PC4
socket_pc4 = socket(AF_INET, SOCK_DGRAM)
socket_pc4.bind(('localhost', 10115))

# Endereços dos PCs permitidos
pc1_address = ('localhost', 10112)
pc3_address = ('localhost', 10114)

# Threads para receber e enviar mensagens
Thread(target=receive_messages, args=(socket_pc4,)).start()
Thread(target=send_message, args=(socket_pc4, pc1_address)).start()
