from socket import *

print("\nPort Scanner TCP\n-----------------------------")

# Inputs
host_alvo = input('Digite o hostname ou o endereço IP do host alvo: ')
print("Digite um intervalo de portas para chegar (ex. 1000 e 2000):")
porta_inicial = int(input("Porta inicial: "))
porta_final = int(input("Porta final: "))


# Status das portas
port_aberta = []
port_fechada = []
port_filtrada = []


#Cria do socket
socketCliente = socket(AF_INET, SOCK_STREAM)
socketCliente.settimeout(0.1)


erro = 0
for port in range(porta_inicial,porta_final,1):

    #Conexao com o servidor
    erro = socketCliente.connect_ex((host_alvo, port))
    if(erro == 0):
        port_aberta.append(port)
    
    elif(erro==11):
        port_filtrada.append(port)
    else:
        print(erro)
        port_fechada.append(port)
    
    
    #Fechamento
    socketCliente.close()



print("\nAnálise das portas:\n-----------------------------")
print("Portas abertas:", port_aberta)
print("Portas fechadas:",port_fechada)
print("Portas filtradas",port_filtrada)

#Fechamento
socketCliente.close()