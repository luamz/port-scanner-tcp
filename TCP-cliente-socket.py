import socket

print("\nPort Scanner TCP\n-----------------------------")

# Inputs
host= input('Digite o hostname ou o endereço IP do host alvo: ')
print("Digite um intervalo de portas para checar (ex. 1000 e 2000):")
porta_inicial = int(input("Porta inicial: "))
porta_final = int(input("Porta final: "))

# Status das portas
abertas = []
fechadas = []
filtradas = []

for porta in range(porta_inicial,porta_final+1,1):

    # Criacao do socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.settimeout(0.1)

    # Tenta conexão com o servidor
    try:
        clientSocket.connect((host,porta))

        # Se consegue conectar
        abertas.append(porta)
    
    # Se não a conexão não é bem sucedida
    ## Se deu time out
    except socket.timeout:
        filtradas.append(porta)
        
    ## Se não deu time out, então está fechada
    except socket.error:
        fechadas.append(porta)

    # Fechamento
    clientSocket.close()
    
print("\nPortas\n-----------------------------")
print("Abertas:", abertas)    
print("Filtradas:", filtradas)
print("Fechadas:", fechadas)

        
