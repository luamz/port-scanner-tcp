from socket import *

#nome do servidor
nomeServidor = raw_input('Nome: ')

#intervalo das portas
ini_port = 11900
final_port = 12010

#auxiliar da porta inicial
port = ini_port

#portas fechadas
port_fechada = []

#porta aberta
port_aberta = []

erro = 0

#Cria do socket
socketCliente = socket(AF_INET, SOCK_STREAM)

while(port < final_port):

    #Conexao com o servidor
    erro = socketCliente.connect_ex((nomeServidor, port))
    if(erro != 0):
        port_fechada.append(port)
    else:
        port_aberta.append(port)

    port += 1


    #Fechamento
    socketCliente.close()

    #Cria do socket
    socketCliente = socket(AF_INET, SOCK_STREAM)

print(port_aberta)
print("\n")
print(port_fechada)

#Fechamento
socketCliente.close()