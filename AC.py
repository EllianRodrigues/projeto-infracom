from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
import rsa 

ac_socket = socket(AF_INET, SOCK_DGRAM)
ac_socket.bind(('localhost', 3500))

print(f"AC iniciado")

localhost_ip = gethostbyname('localhost')

ip_PC1 = (localhost_ip, 10112)
ip_PC2 = (localhost_ip, 10113)
ip_PC3 = (localhost_ip, 10114)
ip_PC4 = (localhost_ip, 10115)
ip_PC5 = (localhost_ip, 10116)
ip_PC6 = (localhost_ip, 10117)

def is_utf8(data):
    try:
        data.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False

while True:
    data, pc_address = ac_socket.recvfrom(1024)
    print(pc_address)
    if pc_address == ip_PC1:
        if data.decode() == "request_public_key_PC1": 
            public_key_PC1, private_key_PC1 = rsa.newkeys(512)  
            private_key_PC1_bytes = private_key_PC1.save_pkcs1()
            ac_socket.sendto(private_key_PC1_bytes, pc_address)
            print(f"Chave privada enviada para o PC 1: {private_key_PC1}")
            
        if data.decode() == "Qual_a_chave_publica_PC2":     
            public_key_PC2_bytes = public_key_PC2.save_pkcs1()
            ac_socket.sendto(public_key_PC2_bytes, pc_address)
            print(f"Chave pública de PC 2 enviada para o PC 1: {public_key_PC2}")
            
    if pc_address == ip_PC2:
        if is_utf8(data) and data.decode() == "request_public_key_PC2": 
            public_key_PC2, private_key_PC2 = rsa.newkeys(512)  
            private_key_PC2_bytes = private_key_PC2.save_pkcs1()
            ac_socket.sendto(private_key_PC2_bytes, pc_address)
            print(f"Chave privada enviada para o PC 2: {private_key_PC2}")
        else:
            print(f"\nMensagem criptografada recebida")
            descriptografado = rsa.decrypt(data, public_key_PC1)
            print(f"Mensagem descriptografada: {descriptografado.decode('utf-8')}")
            ac_socket.sendto(descriptografado, pc_address)
            print(f"Mensagem descriptografada enviada de volta para pc 2")
