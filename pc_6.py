from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

def receive_messages(socket):
    while True:
        message, address = socket.recvfrom(2048)
        print(f"\nMensagem recebida de  {address}: {message.decode()}")

def send_message(socket, address):
    while True:
        target_pc = input("Insira o número do PC (5 or 1): ")
        if target_pc == '5':
            message = input("Insira a mensagem para PC5: ")
            socket.sendto(message.encode(), pc5_address)
        elif target_pc == '1':
            message = input("Insira a mensagem para PC1: ")
            socket.sendto(message.encode(), pc1_address)
        else:
            print("Invalid PC number. Please enter 5 or 1.")

# Configuração do socket do PC6
socket_pc6 = socket(AF_INET, SOCK_DGRAM)
socket_pc6.bind(('localhost', 10117))

# Endereços dos PCs permitidos
pc5_address = ('localhost', 10116)
pc1_address = ('localhost', 10112)

# Threads para receber e enviar mensagens
Thread(target=receive_messages, args=(socket_pc6,)).start()
Thread(target=send_message, args=(socket_pc6, pc5_address)).start()
