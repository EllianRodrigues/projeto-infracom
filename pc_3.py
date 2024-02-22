from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

def receive_messages(socket):
    while True:
        message, address = socket.recvfrom(2048)
        print(f"\nMensagem recebida de  {address}: {message.decode()}")

def send_message(socket, address):
    while True:
        target_pc = input("Insira o número do PC (2 or 4): ")
        if target_pc == '2':
            message = input("Insira a mensagem para PC2: ")
            socket.sendto(message.encode(), pc2_address)
        elif target_pc == '4':
            message = input("Insira a mensagem para PC4: ")
            socket.sendto(message.encode(), pc4_address)
        else:
            print("Número inválido, apenas digite 2 ou 4.")

# Configuração do socket do PC3
socket_pc3 = socket(AF_INET, SOCK_DGRAM)
socket_pc3.bind(('localhost', 10114))

# Endereços dos PCs permitidos
pc2_address = ('localhost', 10113)
pc4_address = ('localhost', 10115)

# Threads para receber e enviar mensagens
Thread(target=receive_messages, args=(socket_pc3,)).start()
Thread(target=send_message, args=(socket_pc3, pc2_address)).start()
