from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from threading import Thread
import rsa
from rsa import verify, sign
from cryptography.fernet import Fernet

import pickle  # Para desserialização dos dados

enivar_primeira_mensagem=True

conexao_pc1=False

localhost_ip = gethostbyname('localhost')

ip_PC1 = (localhost_ip, 10112)

ip_PC1_Para_Key = (localhost_ip, 11111)

ip_PC1_Para_Assinadura = (localhost_ip, 11110)

ip_PC1_Para_Verificacao = (localhost_ip, 11000)

def receive_messages(socket, ac_socket, verification_socket):
    global enivar_primeira_mensagem
    global conexao_pc1
    while True:       
        ciphertext, address = socket.recvfrom(2048)
             
        if address == ip_PC1_Para_Key:
            print("cipher_key: ", ciphertext.hex())
            key_PC1 = rsa.decrypt(ciphertext, private_key)
            print("key: ", key_PC1)
            cipher_suite_PC1 = Fernet(key_PC1)    
                    
        if address == ip_PC1_Para_Assinadura:
            dados_desserializados = pickle.loads(ciphertext)
            # Extrair a mensagem e a assinatura
            sem_assinatura = dados_desserializados['mensagem']
            assinatura = dados_desserializados['assinatura']

            #pegar chave
            ac_socket.sendto("Qual_a_chave_publica_PC1".encode(), ac_address)
            public_key_bytes_PC1, _ = ac_socket.recvfrom(1024)
            public_key_PC1 = rsa.PublicKey.load_pkcs1(public_key_bytes_PC1)
            print(f"Chave publica recebida do AC: {public_key_PC1}") 


            # Verificar a assinatura com a chave pública
            if verify(sem_assinatura.encode(), assinatura, public_key_PC1):
                print("Assinatura válida. Mensagem recebida:", sem_assinatura)
                conexao_pc1=True
                enivar_primeira_mensagem=False
                verification_socket.sendto('Oi, PC1'.encode(),pc1_address)               
            else:
                print("Assinatura inválida.")
                verification_socket.sendto('não_verificado'.encode(),pc1_address) 
                     
        if address == ip_PC1_Para_Verificacao:
            if ciphertext.decode() == "Oi, PC2":
                print("\nPC1 diz: ", ciphertext)
                enivar_primeira_mensagem=False
                conexao_pc1=True
            else:
                print("\nPC1 diz: ", ciphertext)            
                                                              
        if address == ip_PC1 and conexao_pc1:
            print(f"\nMensagem criptografada recebida de {address} mensagem criptografada: {ciphertext}")           
            plaintext = cipher_suite_PC1.decrypt(ciphertext).decode()
            print(f'\nDescriptografado: {plaintext}')
          
            
            
            
        
def send_message(socket, address, ac_socket):
    while True:
        target_pc = input("Insira o número do PC (1 or 3): ")
        if target_pc == '1':
            
            if (enivar_primeira_mensagem):
                
                sem_assinatura = input("Insira a primeira mensagem para a conexão: ")
                assinatura = sign(sem_assinatura.encode(), private_key, 'SHA-256')
                
                dados_enviar = {'mensagem': sem_assinatura, 'assinatura': assinatura}

                # Serializar os dados
                dados_serializados = pickle.dumps(dados_enviar)

                # Enviar os dados serializados
                assing_socket.sendto(dados_serializados, pc1_address)
                
                #mandar_primeira_mensagen=False
            
            if(enivar_primeira_mensagem==False):
                ac_socket.sendto("Qual_a_chave_publica_PC1".encode(), ac_address)
                public_key_bytes_PC1, _ = ac_socket.recvfrom(1024)
                public_key_PC1 = rsa.PublicKey.load_pkcs1(public_key_bytes_PC1)
                print(f"Chave publica recebida do AC: {public_key_PC1}") 
                
                key = Fernet.generate_key()
                print("key: ", key)
                cipher_key = rsa.encrypt(key, public_key_PC1)
                print("cypher Key: ", cipher_key)
                ac_socket.sendto(cipher_key, pc1_address)
                        
                cipher_suite = Fernet(key)
                            
                message = input("Insira a mensagem para PC1: ")
                message_bytes = cipher_suite.encrypt(message.encode())           
                socket.sendto(message_bytes, pc1_address)  
            
                print(f'mensagem criptografada enviada: {message_bytes}')  
        
        elif target_pc == '3':
            message = input("Insira a mensagem para PC3: ")
            socket.sendto(message.encode(), pc3_address)
        else:
            print("Número inválido, apenas digite 1 ou 3.")

# Configuração do socket do PC2
socket_pc2 = socket(AF_INET, SOCK_DGRAM)
socket_pc2.bind(('localhost', 10113))

# Configuração do socket para comunicação com o AC e PC para keys
ac_socket = socket(AF_INET, SOCK_DGRAM)
ac_socket.bind(('localhost', 22222))

# configuração para devolver assinado
assing_socket = socket(AF_INET,SOCK_DGRAM)
assing_socket.bind(('localhost', 22220))

#configuração para responder a verificação
verification_socket = socket (AF_INET,SOCK_DGRAM)
verification_socket.bind(('localhost',22000))

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
Thread(target=receive_messages, args=(socket_pc2,ac_socket,verification_socket)).start()
Thread(target=send_message, args=(socket_pc2, pc3_address, ac_socket)).start()
