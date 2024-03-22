from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from threading import Thread
import rsa 
from rsa import sign, verify
from cryptography.fernet import Fernet
import pickle  # Para serialização dos dados

assign_socket = socket(AF_INET,SOCK_DGRAM)
assign_socket.bind(('localhost', 11110))

ac_socket = socket(AF_INET, SOCK_DGRAM)
ac_socket.bind(('localhost', 11111))

verification_socket = socket (AF_INET,SOCK_DGRAM)
verification_socket.bind(('localhost',11000))

mandar_primeira_mensagem = True
conexao_pc = False

def receive_messages(socket, address_clockwise, address_anticlockwise):
    global conexao_pc

    while True:
        message, address = socket.recvfrom(2048)
        print(f"\nMensagem recebida pela porta: {address} | ", end="")
        decode_message = eval(message.decode())
        if (decode_message['token']):
            if (decode_message['destination_address'] == 10112):
                sem_assinatura = eval(decode_message['message'])['mensagem']
                assinatura = eval(decode_message['message'])['assinatura']
                
                #pegar chave
                ac_socket.sendto(f"Qual_a_chave_publica_PC{str(decode_message['source_address'])}".encode(), ac_address)
                public_key_bytes_PC, _ = ac_socket.recvfrom(1024)
                public_key_PC = rsa.PublicKey.load_pkcs1(public_key_bytes_PC)
                print(f"Chave publica recebida do AC: {public_key_PC}")

                # Verificar a assinatura com a chave pública
                if verify(sem_assinatura.encode(), assinatura, public_key_PC):
                    print("Assinatura válida. Mensagem recebida:", sem_assinatura)
                    conexao_pc=True
                    # Envia resposta de volta
                    datagram = make_pseudo_datagram(f"MENSAGEM VERIFICADA!!! OI, PC{str(decode_message['source_address'])}", decode_message['source_address'], False)   
                    print("enviando confirmação para" + str(decode_message['source_address']))
                    if (roteamento(10112, ('tantofaz', decode_message['source_address'])) == "clockwise"):
                        socket.sendto(datagram.encode(), address_clockwise)
                    else:
                        socket.sendto(datagram.encode(), address_anticlockwise)
            else:
                #Encaminhamento (não mexer aqui!)
                encaminha(socket, address_clockwise, address_anticlockwise, address, message)
        else: 
            if (decode_message['destination_address'] == 10112):
                print("Destinatario valido\nMensagem de: " + str(decode_message['source_address']) + "\nBody: " + decode_message['message'])
                #Responde as mensagem, exceto a de confirmação
                if (decode_message['message'] != "Mensagem recebida" and decode_message['message'] != "MENSAGEM VERIFICADA!!! OI, PC10112"):
                    # Envia resposta de volta
                    print("Enviando confirmação de recebimento...")
                    datagram = make_pseudo_datagram("Mensagem recebida", decode_message['source_address'], False)
                    if (roteamento(10112, ('tantofaz', decode_message['source_address'])) == "clockwise"):
                        socket.sendto(datagram.encode(), address_clockwise)
                    else:
                        socket.sendto(datagram.encode(), address_anticlockwise)
                #Se a mensagem for para outro PC, eu encaminho no sentido contrario que eu recebi
                pedir_input()
            else: 
                #Encaminhamento (não mexer aqui!)
                encaminha(socket, address_clockwise, address_anticlockwise, address, message)
        
        

def send_message(socket, address_clockwise, address_anticlockwise):
    while True:
        message = input()
        # Escreva a mensagem como parametro da função send
        send(socket, address_clockwise, address_anticlockwise, message)

def send(socket, address_clockwise, address_anticlockwise, message):
    global mandar_primeira_mensagem
    for destination_address in destination_address_map.values():
            ##### FAZER O MAPEAMENTO DAS CHAVES PARA OS ENDEREÇOS DOS PCS
            if (destination_address[1] != 10112):
                if (mandar_primeira_mensagem):                
                    assinatura = sign(message.encode(), private_key, 'SHA-256')
                    dados_enviar = {'mensagem': message, 'assinatura': assinatura}
                    # Serializar os dados
                    dados_serializados = str(dados_enviar)
                    print(dados_serializados)
                    # Enviar os dados serializados
                    datagram = make_pseudo_datagram(dados_serializados, destination_address[1], True)
                    if (roteamento(10112, destination_address) == "clockwise"):
                        socket.sendto(datagram.encode(), address_clockwise)
                    else:
                        socket.sendto(datagram.encode(), address_anticlockwise)
                else:
                    datagram = make_pseudo_datagram(message, destination_address[1], False)
                    # Cria um pacote com o endereço de src, dest e a mensagem
                    # Agora precisamos fazer o roteamento para enviar o pacote
                    if (roteamento(10112, destination_address) == "clockwise"):
                        socket.sendto(datagram.encode(), address_clockwise)
                    else:
                        socket.sendto(datagram.encode(), address_anticlockwise)
    mandar_primeira_mensagem=False

def encaminha(socket, address_clockwise, address_anticlockwise, address, message):
    if (address[1] == address_anticlockwise[1]):
            print("Destinatario invalido, encaminhando...")
            #Encaminha para o sentido horario
            socket.sendto(message, address_clockwise)
            pedir_input()
    else:
        print("Destinatario invalido, encaminhando...")
        #Encaminha para o sentido anti-horario
        socket.sendto(message, address_anticlockwise)
        pedir_input()


def make_pseudo_datagram(message, destination_address, is_token):
    message = {
        'source_address': 10112,
        'destination_address': destination_address,
        'token': is_token,
        'message': message
    }
    return str(message)

def roteamento(source_address, destination_address):
    # Implementar roteamento
    result = source_address - destination_address[1]
    if (result == -2 or result == -1 or result == 4 or result == 5):
        return "clockwise"
    else:
        return "anticlockwise"


# Configuração do socket do PC1
socket_pc1 = socket(AF_INET, SOCK_DGRAM)
socket_pc1.bind(('localhost', 10112))

# Endereços dos PCs permitidos
destination_address_map = {
    "1": ('localhost', 10112),
    '2': ('localhost', 10113),
    '3': ('localhost', 10114),
    '4': ('localhost', 10115),
    '5': ('localhost', 10116),
    '6': ('localhost', 10117)
}

clockwise_address = destination_address_map['2']
anticlockwise_address = destination_address_map['6']

def pedir_input():
    #Exibe mensagem para não bugar UI do CLI
    print("===============================================")
    print("Escreva a mensagem para Broadcast abaixo: ")

#conexão com o AC
ac_address = ('localhost', 3500)
socket_pc1.sendto("request_public_key_PC1".encode(), ac_address)
private_key_bytes, _ = socket_pc1.recvfrom(1024)
private_key = rsa.PrivateKey.load_pkcs1(private_key_bytes)

print("Bem vindo ao PC1")
pedir_input()
# Threads para receber e enviar mensagens
Thread(target=receive_messages, args=(socket_pc1, clockwise_address, anticlockwise_address)).start()
Thread(target=send_message, args=(socket_pc1, clockwise_address, anticlockwise_address)).start()
