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

ip_PC1_Para_Portas = (localhost_ip, 11111)
ip_PC2_Para_Portas = (localhost_ip, 22222)
ip_PC3_Para_Portas = (localhost_ip, 33333)
ip_PC4_Para_Portas = (localhost_ip, 44444)
ip_PC5_Para_Portas = (localhost_ip, 55555)
ip_PC6_Para_Portas = (localhost_ip, 60000)


while True:
    data, pc_address = ac_socket.recvfrom(1024)
    print(pc_address)
    #PC1
    if pc_address == ip_PC1:
        if data.decode() == "request_public_key_PC1": 
            public_key_PC1, private_key_PC1 = rsa.newkeys(512)  
            private_key_PC1_bytes = private_key_PC1.save_pkcs1()
            ac_socket.sendto(private_key_PC1_bytes, pc_address)
            print(f"Chave privada enviada para o PC 1: {private_key_PC1}")         
    if pc_address == ip_PC1_Para_Portas:        
        #PC2
        if data.decode() == "Qual_a_chave_publica_PC10113":     
            public_key_PC2_bytes = public_key_PC2.save_pkcs1()
            ac_socket.sendto(public_key_PC2_bytes, pc_address)
            print(f"Chave pública de PC 2 enviada para o PC 1: {public_key_PC2}")
        #PC3
        if data.decode() == "Qual_a_chave_publica_PC10114":     
            public_key_PC3_bytes = public_key_PC3.save_pkcs1()
            ac_socket.sendto(public_key_PC3_bytes, pc_address)
            print(f"Chave pública de PC 3 enviada para o PC 1: {public_key_PC3}")
        #PC4
        if data.decode() == "Qual_a_chave_publica_PC10115":     
            public_key_PC4_bytes = public_key_PC4.save_pkcs1()
            ac_socket.sendto(public_key_PC4_bytes, pc_address)
            print(f"Chave pública de PC 4 enviada para o PC 1: {public_key_PC4}")
        #PC5
        if data.decode() == "Qual_a_chave_publica_PC10116":     
            public_key_PC5_bytes = public_key_PC5.save_pkcs1()
            ac_socket.sendto(public_key_PC5_bytes, pc_address)
            print(f"Chave pública de PC 5 enviada para o PC 1: {public_key_PC5}")
        #PC6
        if data.decode() == "Qual_a_chave_publica_PC10117":     
            public_key_PC6_bytes = public_key_PC6.save_pkcs1()
            ac_socket.sendto(public_key_PC6_bytes, pc_address)
            print(f"Chave pública de PC 6 enviada para o PC 1: {public_key_PC6}")
 
    #PC2
    if pc_address == ip_PC2:
        if data.decode() == "request_public_key_PC2": 
            public_key_PC2, private_key_PC2 = rsa.newkeys(512)  
            private_key_PC2_bytes = private_key_PC2.save_pkcs1()
            ac_socket.sendto(private_key_PC2_bytes, pc_address)
            print(f"Chave privada enviada para o PC 2: {private_key_PC2}")
    if pc_address == ip_PC2_Para_Portas: 
        #PC1
        if data.decode() == "Qual_a_chave_publica_PC10112":     
            public_key_PC1_bytes = public_key_PC1.save_pkcs1()
            ac_socket.sendto(public_key_PC1_bytes, pc_address)
            print(f"Chave pública de PC 1 enviada para o PC 2: {public_key_PC2}")
        #PC3
        if data.decode() == "Qual_a_chave_publica_PC10114":     
            public_key_PC3_bytes = public_key_PC3.save_pkcs1()
            ac_socket.sendto(public_key_PC3_bytes, pc_address)
            print(f"Chave pública de PC 3 enviada para o PC 1: {public_key_PC3}")
        #PC4
        if data.decode() == "Qual_a_chave_publica_PC10115":     
            public_key_PC4_bytes = public_key_PC4.save_pkcs1()
            ac_socket.sendto(public_key_PC4_bytes, pc_address)
            print(f"Chave pública de PC 4 enviada para o PC 1: {public_key_PC4}")
        #PC5
        if data.decode() == "Qual_a_chave_publica_PC10116":     
            public_key_PC5_bytes = public_key_PC5.save_pkcs1()
            ac_socket.sendto(public_key_PC5_bytes, pc_address)
            print(f"Chave pública de PC 5 enviada para o PC 1: {public_key_PC5}")
        #PC6
        if data.decode() == "Qual_a_chave_publica_PC10117":     
            public_key_PC6_bytes = public_key_PC6.save_pkcs1()
            ac_socket.sendto(public_key_PC6_bytes, pc_address)
            print(f"Chave pública de PC 6 enviada para o PC 1: {public_key_PC6}")
            

    #PC3
    if pc_address == ip_PC3:
        if data.decode() == "request_public_key_PC3": 
            public_key_PC3, private_key_PC3 = rsa.newkeys(512)  
            private_key_PC3_bytes = private_key_PC3.save_pkcs1()
            ac_socket.sendto(private_key_PC3_bytes, pc_address)
            print(f"Chave privada enviada para o PC 3: {private_key_PC3}")
    if pc_address == ip_PC3_Para_Portas:
        #PC1
        if data.decode() == "Qual_a_chave_publica_PC10112":     
            public_key_PC1_bytes = public_key_PC1.save_pkcs1()
            ac_socket.sendto(public_key_PC1_bytes, pc_address)
            print(f"Chave pública de PC 1 enviada para o PC 2: {public_key_PC2}")
        #PC2
        if data.decode() == "Qual_a_chave_publica_PC10113":     
            public_key_PC2_bytes = public_key_PC2.save_pkcs1()
            ac_socket.sendto(public_key_PC2_bytes, pc_address)
            print(f"Chave pública de PC 2 enviada para o PC 1: {public_key_PC2}")
        #PC4
        if data.decode() == "Qual_a_chave_publica_PC10115":     
            public_key_PC4_bytes = public_key_PC4.save_pkcs1()
            ac_socket.sendto(public_key_PC4_bytes, pc_address)
            print(f"Chave pública de PC 4 enviada para o PC 1: {public_key_PC4}")
        #PC5
        if data.decode() == "Qual_a_chave_publica_PC10116":     
            public_key_PC5_bytes = public_key_PC5.save_pkcs1()
            ac_socket.sendto(public_key_PC5_bytes, pc_address)
            print(f"Chave pública de PC 5 enviada para o PC 1: {public_key_PC5}")
        #PC6
        if data.decode() == "Qual_a_chave_publica_PC10117":     
            public_key_PC6_bytes = public_key_PC6.save_pkcs1()
            ac_socket.sendto(public_key_PC6_bytes, pc_address)
            print(f"Chave pública de PC 6 enviada para o PC 1: {public_key_PC6}")

    #PC4
    if pc_address == ip_PC4:
            if data.decode() == "request_public_key_PC4": 
                public_key_PC4, private_key_PC4 = rsa.newkeys(512)  
                private_key_PC4_bytes = private_key_PC4.save_pkcs1()
                ac_socket.sendto(private_key_PC4_bytes, pc_address)
                print(f"Chave privada enviada para o PC 4: {private_key_PC4}")
    if pc_address == ip_PC4_Para_Portas:
        #PC1
        if data.decode() == "Qual_a_chave_publica_PC10112":     
            public_key_PC1_bytes = public_key_PC1.save_pkcs1()
            ac_socket.sendto(public_key_PC1_bytes, pc_address)
            print(f"Chave pública de PC 1 enviada para o PC 2: {public_key_PC2}")
        #PC2
        if data.decode() == "Qual_a_chave_publica_PC10113":     
            public_key_PC2_bytes = public_key_PC2.save_pkcs1()
            ac_socket.sendto(public_key_PC2_bytes, pc_address)
            print(f"Chave pública de PC 2 enviada para o PC 1: {public_key_PC2}")
        #PC3
        if data.decode() == "Qual_a_chave_publica_PC10114":     
            public_key_PC3_bytes = public_key_PC3.save_pkcs1()
            ac_socket.sendto(public_key_PC3_bytes, pc_address)
            print(f"Chave pública de PC 3 enviada para o PC 1: {public_key_PC3}")
        #PC5
        if data.decode() == "Qual_a_chave_publica_PC10116":     
            public_key_PC5_bytes = public_key_PC5.save_pkcs1()
            ac_socket.sendto(public_key_PC5_bytes, pc_address)
            print(f"Chave pública de PC 5 enviada para o PC 1: {public_key_PC5}")
        #PC6
        if data.decode() == "Qual_a_chave_publica_PC10117":     
            public_key_PC6_bytes = public_key_PC6.save_pkcs1()
            ac_socket.sendto(public_key_PC6_bytes, pc_address)
            print(f"Chave pública de PC 6 enviada para o PC 1: {public_key_PC6}")

    #PC5
    if pc_address == ip_PC5:
            if data.decode() == "request_public_key_PC5": 
                public_key_PC5, private_key_PC5 = rsa.newkeys(512)  
                private_key_PC5_bytes = private_key_PC5.save_pkcs1()
                ac_socket.sendto(private_key_PC5_bytes, pc_address)
                print(f"Chave privada enviada para o PC 5: {private_key_PC5}")
    if pc_address == ip_PC5_Para_Portas:
        #PC1
        if data.decode() == "Qual_a_chave_publica_PC10112":     
            public_key_PC1_bytes = public_key_PC1.save_pkcs1()
            ac_socket.sendto(public_key_PC1_bytes, pc_address)
            print(f"Chave pública de PC 1 enviada para o PC 2: {public_key_PC2}")
        #PC2
        if data.decode() == "Qual_a_chave_publica_PC10113":     
            public_key_PC2_bytes = public_key_PC2.save_pkcs1()
            ac_socket.sendto(public_key_PC2_bytes, pc_address)
            print(f"Chave pública de PC 2 enviada para o PC 1: {public_key_PC2}")
        #PC3
        if data.decode() == "Qual_a_chave_publica_PC10114":     
            public_key_PC3_bytes = public_key_PC3.save_pkcs1()
            ac_socket.sendto(public_key_PC3_bytes, pc_address)
            print(f"Chave pública de PC 3 enviada para o PC 1: {public_key_PC3}")
        #PC4
        if data.decode() == "Qual_a_chave_publica_PC10115":     
            public_key_PC4_bytes = public_key_PC4.save_pkcs1()
            ac_socket.sendto(public_key_PC4_bytes, pc_address)
            print(f"Chave pública de PC 4 enviada para o PC 1: {public_key_PC4}")
        #PC6
        if data.decode() == "Qual_a_chave_publica_PC10117":     
            public_key_PC6_bytes = public_key_PC6.save_pkcs1()
            ac_socket.sendto(public_key_PC6_bytes, pc_address)
            print(f"Chave pública de PC 6 enviada para o PC 1: {public_key_PC6}")


    #PC6
    if pc_address == ip_PC6:
        if data.decode() == "request_public_key_PC6": 
            public_key_PC6, private_key_PC6 = rsa.newkeys(512)  
            private_key_PC6_bytes = private_key_PC6.save_pkcs1()
            ac_socket.sendto(private_key_PC6_bytes, pc_address)
            print(f"Chave privada enviada para o PC 6: {private_key_PC6}")
    if pc_address == ip_PC6_Para_Portas:
            #PC1
            if data.decode() == "Qual_a_chave_publica_PC10112":     
                public_key_PC1_bytes = public_key_PC1.save_pkcs1()
                ac_socket.sendto(public_key_PC1_bytes, pc_address)
                print(f"Chave pública de PC 1 enviada para o PC 2: {public_key_PC2}")
            #PC2
            if data.decode() == "Qual_a_chave_publica_PC10113":     
                public_key_PC2_bytes = public_key_PC2.save_pkcs1()
                ac_socket.sendto(public_key_PC2_bytes, pc_address)
                print(f"Chave pública de PC 2 enviada para o PC 1: {public_key_PC2}")
            #PC3
            if data.decode() == "Qual_a_chave_publica_PC10114":     
                public_key_PC3_bytes = public_key_PC3.save_pkcs1()
                ac_socket.sendto(public_key_PC3_bytes, pc_address)
                print(f"Chave pública de PC 3 enviada para o PC 1: {public_key_PC3}")
            #PC4
            if data.decode() == "Qual_a_chave_publica_PC10115":     
                public_key_PC4_bytes = public_key_PC4.save_pkcs1()
                ac_socket.sendto(public_key_PC4_bytes, pc_address)
                print(f"Chave pública de PC 4 enviada para o PC 1: {public_key_PC4}")
            #PC5
            if data.decode() == "Qual_a_chave_publica_PC10116":     
                public_key_PC5_bytes = public_key_PC5.save_pkcs1()
                ac_socket.sendto(public_key_PC5_bytes, pc_address)
                print(f"Chave pública de PC 5 enviada para o PC 1: {public_key_PC5}")
    