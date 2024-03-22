from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from threading import Thread
import rsa 
from rsa import sign, verify
from cryptography.fernet import Fernet
import pickle  # Para serialização dos dados

mandar_primeira_mensagen=True

conexao_PC2=False

localhost_ip = gethostbyname('localhost')

ip_PC2 = (localhost_ip, 10113)

ip_PC2_Para_Key = (localhost_ip, 22222)

ip_PC2_Para_Assinatura = (localhost_ip, 22220)

ip_PC2_Para_Verificacao = (localhost_ip, 22000)


def receive_messages(socket):
    global mandar_primeira_mensagen
    global conexao_PC2
    while True:   
        ciphertext, address = socket.recvfrom(2048)
        if address == ip_PC2_Para_Key:
            print("cipher_key: ", ciphertext.hex())
            key_PC2 = rsa.decrypt(ciphertext, private_key)
            print("key: ", key_PC2)
            cipher_suite_PC2 = Fernet(key_PC2)
      
        if address == ip_PC2_Para_Assinatura:
            dados_desserializados = pickle.loads(ciphertext)
            # Extrair a mensagem e a assinatura
            sem_assinatura = dados_desserializados['mensagem']
            assinatura = dados_desserializados['assinatura']

            #pegar chave
            ac_socket.sendto("Qual_a_chave_publica_PC2".encode(), ac_address)
            public_key_bytes_PC2, _ = ac_socket.recvfrom(1024)
            public_key_PC2 = rsa.PublicKey.load_pkcs1(public_key_bytes_PC2)
            print(f"Chave publica recebida do AC: {public_key_PC2}") 


            # Verificar a assinatura com a chave pública
            if verify(sem_assinatura.encode(), assinatura, public_key_PC2):
                print("Assinatura válida. Mensagem recebida:", sem_assinatura)
                conexao_PC2=True
                mandar_primeira_mensagen=False
                verification_socket.sendto('Oi, PC2'.encode(),pc2_address)               
            else:
                print("Assinatura inválida.")
                verification_socket.sendto('não_verificado'.encode(),pc2_address) 

      
        if address == ip_PC2_Para_Verificacao:
            if ciphertext.decode() == "Oi, PC1":
                print("PC2 diz: ", ciphertext)
                mandar_primeira_mensagen=False
                conexao_PC2=True
            #else:
                #print("PC2 diz: ", ciphertext)
            
        if address == ip_PC2 and conexao_PC2: 
            print(f"\nMensagem criptografada recebida de {address} mensagem criptografada: {ciphertext}")           
            plaintext = cipher_suite_PC2.decrypt(ciphertext).decode()
            print(f'\nDescriptografado: {plaintext}')

def send_message(socket, address, ac_socket, assing_socket):
    global mandar_primeira_mensagen
    while True:
        target_pc = input("Insira o número do PC (2 or 6): ")
        if target_pc == '2':
                                                                                                    
            if (mandar_primeira_mensagen):
                
                sem_assinatura = input("Insira a primeira mensagem para a conexão: ")
                assinatura = sign(sem_assinatura.encode(), private_key, 'SHA-256')
                
                dados_enviar = {'mensagem': sem_assinatura, 'assinatura': assinatura}

                # Serializar os dados
                dados_serializados = pickle.dumps(dados_enviar)

                # Enviar os dados serializados
                assing_socket.sendto(dados_serializados, pc2_address)
                
                #mandar_primeira_mensagen=False
                                            
            if(mandar_primeira_mensagen==False):    
                                                                
                ac_socket.sendto("Qual_a_chave_publica_PC2".encode(), ac_address)
                public_key_bytes_PC2, _ = ac_socket.recvfrom(1024)
                public_key_PC2 = rsa.PublicKey.load_pkcs1(public_key_bytes_PC2)
                print(f"Chave publica recebida do AC: {public_key_PC2}")  
                
                key = Fernet.generate_key()
                print("key: ", key)
                cipher_key = rsa.encrypt(key, public_key_PC2)
                print("cypher Key: ", cipher_key)
                ac_socket.sendto(cipher_key, pc2_address)
                
                cipher_suite = Fernet(key)
                            
                message = input("Insira a mensagem para PC2: ")
                message_bytes = cipher_suite.encrypt(message.encode())           
                socket.sendto(message_bytes, pc2_address)  
                
                print(f'mensagem criptografada enviada: {message_bytes}')   
                                   
        elif target_pc == '6':
            message = input("Insira a mensagem para PC6: ")
            socket.sendto(message.encode(), pc6_address)
        else:
            print("Número inválido, apenas digite 2 ou 6.")

# Configuração do socket do PC1
socket_pc1 = socket(AF_INET, SOCK_DGRAM)
socket_pc1.bind(('localhost', 10112))

# Configuração do socket para comunicação com o AC  e PC para keys
ac_socket = socket(AF_INET, SOCK_DGRAM)
ac_socket.bind(('localhost', 11111))

# configuração para devolver assinado
assing_socket = socket(AF_INET,SOCK_DGRAM)
assing_socket.bind(('localhost', 11110))

#configuração para responder a verificação
verification_socket = socket (AF_INET,SOCK_DGRAM)
verification_socket.bind(('localhost',11000))


# Endereços dos PCs permitidos
pc2_address = ('localhost', 10113)
pc6_address = ('localhost', 10117)

#conexão com o AC
ac_address = ('localhost', 3500)
socket_pc1.sendto("request_public_key_PC1".encode(), ac_address)
private_key_bytes, _ = socket_pc1.recvfrom(1024)
private_key = rsa.PrivateKey.load_pkcs1(private_key_bytes)
print(f"Chave privada recebida do AC: {private_key}")


# Threads para receber e enviar mensagens
Thread(target=receive_messages, args=(socket_pc1,)).start()
Thread(target=send_message, args=(socket_pc1, pc2_address, ac_socket, assing_socket)).start()
