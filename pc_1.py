from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import rsa 


def receive_messages(socket):
    while True:   
        ciphertext, address = socket.recvfrom(2048)
        print(f"\nMensagem criptografada recebida de {address} mensagem criptografada: {ciphertext}")
        plaintext = rsa.decrypt(ciphertext, private_key)
        print(f'\nDescriptografado: {plaintext.decode("utf-8")}')

def send_message(socket, address, ac_socket):
   
    while True:
        target_pc = input("Insira o número do PC (2 or 6): ")
        if target_pc == '2':
                                  
            ac_socket.sendto("Qual_a_chave_publica_PC2".encode(), ac_address)
            public_key_bytes_PC2, _ = ac_socket.recvfrom(1024)
            public_key_PC2 = rsa.PublicKey.load_pkcs1(public_key_bytes_PC2)
            print(f"Chave publica recebida do AC: {public_key_PC2}")         
                           
            message = input("Insira a mensagem para PC2: ")
            message_bytes = message.encode('utf-8')
            
            ciphertext = rsa.encrypt(message_bytes, public_key_PC2)
            socket.sendto(ciphertext, pc2_address)  
            
            print(f'mensagem criptografada enviada: {ciphertext}')   
                  
        elif target_pc == '6':
            message = input("Insira a mensagem para PC6: ")
            socket.sendto(message.encode(), pc6_address)
        else:
            print("Número inválido, apenas digite 2 ou 6.")

# Configuração do socket do PC1
socket_pc1 = socket(AF_INET, SOCK_DGRAM)
socket_pc1.bind(('localhost', 10112))

# Configuração do socket para comunicação com o AC
ac_socket = socket(AF_INET, SOCK_DGRAM)
ac_socket.bind(('localhost', 11111))

# Endereços dos PCs permitidos
pc2_address = ('localhost', 10113)
pc6_address = ('localhost', 10117)

#conexão com o AC
ac_address = ('localhost', 3500)
socket_pc1.sendto("request_public_key_PC1".encode(), ac_address)
private_key_bytes, _ = socket_pc1.recvfrom(1024)
private_key = rsa.PrivateKey.load_pkcs1(private_key_bytes)
print(f"Chave privada recebida do AC: {private_key}")

#socket_pc1.sendto("Qual_a_chave_publica_PC2".encode(), ac_address)
#public_key_bytes_PC2, _ = socket_pc1.recvfrom(1024)
#public_key_PC2 = rsa.PublicKey.load_pkcs1(public_key_bytes_PC2)
#print(f"Chave publica recebida do AC: {public_key_PC2}")

# Threads para receber e enviar mensagens
Thread(target=receive_messages, args=(socket_pc1,)).start()
Thread(target=send_message, args=(socket_pc1, pc2_address, ac_socket)).start()
