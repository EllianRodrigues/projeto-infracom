from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

def receive_messages(socket, address_clockwise, address_anticlockwise):
    while True:
        message, address = socket.recvfrom(2048)
        print(f"\nMensagem recebida pela porta: {address} | ", end="")
        decode_message = eval(message.decode())
        if (decode_message['destination_address'] == 10117):
            print("Destinatario valido\nMensagem de: " + str(decode_message['source_address']) + "\nBody: " + decode_message['message'])
            #Responde as mensagem, exceto a de confirmação
            if (decode_message['message'] != "Mensagem recebida"):
                # Envia resposta de volta
                print("Enviando confirmação de recebimento...")
                response = make_pseudo_datagram("Mensagem recebida", decode_message['source_address'])
                socket.sendto(response.encode(), ('localhost', decode_message['source_address']))
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
    for destination_address in destination_address_map.values():
            if (destination_address[1] != 10117):
                datagram = make_pseudo_datagram(message, destination_address[1])
                # Cria um pacote com o endereço de src, dest e a mensagem
                # Agora precisamos fazer o roteamento para enviar o pacote
                if (roteamento(10112, destination_address) == "clockwise"):
                    socket.sendto(datagram.encode(), address_clockwise)
                else:
                    socket.sendto(datagram.encode(), address_anticlockwise)

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


def make_pseudo_datagram(message, destination_address):
    message = {
        'source_address': 10117,
        'destination_address': destination_address,
        'message': message
    }
    return str(message)

def roteamento(source_address, destination_address):
    # Implementar roteamento
    result = source_address - destination_address[1]
    if (result == -2 or result == -1 or result == 4 or result == 5 or result == 3 or result == -3):
        return "clockwise"
    else:
        return "anticlockwise"


# Configuração do socket do PC1
socket_pc1 = socket(AF_INET, SOCK_DGRAM)
socket_pc1.bind(('localhost', 10117))

# Endereços dos PCs permitidos
destination_address_map = {
    "1": ('localhost', 10112),
    '2': ('localhost', 10113),
    '3': ('localhost', 10114),
    '4': ('localhost', 10115),
    '5': ('localhost', 10116),
    '6': ('localhost', 10117)
}

clockwise_address = destination_address_map['1']
anticlockwise_address = destination_address_map['5']

def pedir_input():
    #Exibe mensagem para não bugar UI do CLI
    print("===============================================")
    print("Escreva a mensagem para Broadcast abaixo: ")

print("Bem vindo ao PC6")
pedir_input()
# Threads para receber e enviar mensagens
Thread(target=receive_messages, args=(socket_pc1, clockwise_address, anticlockwise_address)).start()
Thread(target=send_message, args=(socket_pc1, clockwise_address, anticlockwise_address)).start()
