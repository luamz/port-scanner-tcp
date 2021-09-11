import socket

# Numero de porta na qual o servidor estará esperando conexões.
serverPort = 12000

# Criar o socket. AF_INET e SOCK_STREAM indicam TCP.
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associar o socket a porta escolhida. Primeiro argumento vazio indica
# que desejamos aceitar conexoes em qualquer interface de rede desse host
serverSocket.bind(('', serverPort))

# Habilitar socket para aceitar conexoes. O argumento 1 indica que até
# uma conexão será deixada em espera, caso receba multiplas conexões
# simultâneas
serverSocket.listen(1)

print ('O servidor está pronto para receber conexões')

# Loop infinito: servidor é capaz de tratar múltiplas conexões
while 1:

    # Aguardar nova conexao
    print ('Aguardando conexao...')
    connectionSocket, addr = serverSocket.accept()
    print ('Ok!')
    # Fechamento
    print ('Fechando socket...')
    connectionSocket.close()

