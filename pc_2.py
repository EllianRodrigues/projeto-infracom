from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import rsa

def receive_messages(socket):
    while True:
        ciphertext, address = socket.recvfrom(2048)
        print(f"\nMensagem criptografada recebida de {address}")

        plaintext = rsa.decrypt(ciphertext, private_key)

        print(f'\nDescriptografado: {plaintext.decode("utf-8")}')
        
def send_message(socket, address):
    while True:
        target_pc = input("Insira o número do PC (1 or 3): ")
        if target_pc == '1':
            message = input("Insira a mensagem para PC1: ")
            socket.sendto(message.encode(), pc1_address)
        elif target_pc == '3':
            message = input("Insira a mensagem para PC3: ")
            socket.sendto(message.encode(), pc3_address)
        else:
            print("Número inválido, apenas digite 1 ou 3.")

# Configuração do socket do PC2
socket_pc2 = socket(AF_INET, SOCK_DGRAM)
socket_pc2.bind(('localhost', 10113))

# Endereços dos PCs permitidos
pc1_address = ('localhost', 10112)
pc3_address = ('localhost', 10114)



#conexão com o AC
ac_address = ('localhost', 3500)
socket_pc2.sendto("request_public_key_PC2".encode(), ac_address)
private_key_bytes, _ = socket_pc2.recvfrom(1024)
private_key = rsa.PrivateKey.load_pkcs1(private_key_bytes)
print(f"Chave privada recebida do AC: {private_key}")


# Threads para receber e enviar mensagens
Thread(target=receive_messages, args=(socket_pc2,)).start()
Thread(target=send_message, args=(socket_pc2, pc3_address)).start()
