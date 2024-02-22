from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

def receive_messages(socket):
    while True:
        message, address = socket.recvfrom(2048)
        print(f"\nMensagem recebida de  {address}: {message.decode()}")

def send_message(socket, address):
    while True:
        target_pc = input("Insira o número do PC (3 or 5): ")
        if target_pc == '3':
            message = input("Insira a mensagem para PC3: ")
            socket.sendto(message.encode(), pc3_address)
        elif target_pc == '5':
            message = input("Insira a mensagem para PC5: ")
            socket.sendto(message.encode(), pc5_address)
        else:
            print("Número inválido, apenas digite 3 ou 5.")

# Configuração do socket do PC4
socket_pc4 = socket(AF_INET, SOCK_DGRAM)
socket_pc4.bind(('localhost', 10115))

# Endereços dos PCs permitidos
pc3_address = ('localhost', 10114)
pc5_address = ('localhost', 10116)

# Threads para receber e enviar mensagens
Thread(target=receive_messages, args=(socket_pc4,)).start()
Thread(target=send_message, args=(socket_pc4, pc3_address)).start()
