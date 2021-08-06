import socket

# Numero de porta na qual o servidor estara esperando conexoes.
serverPort = 12000

# Criar o socket. AF_INET e SOCK_STREAM indicam TCP.
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associar o socket a porta escolhida. Primeiro argumento vazio indica
# que desejamos aceitar conexoes em qualquer interface de rede desse host
serverSocket.bind(('', serverPort))

# Habilitar socket para aceitar conexoes. O argumento 1 indica que ate
# uma conexao sera deixada em espera, caso recebamos multiplas conexoes
# simultaneas
serverSocket.listen(1)

print ('O servidor esta pronto para receber conexoes')

# Loop infinito: servidor eh capaz de tratar multiplas conexoes
while 1:

    # Aguardar nova conexao
    print ('Aguardando conexao...')
    connectionSocket, addr = serverSocket.accept()
    print ('Ok!')
    # Fechamento
    print ('Fechando socket...')
    connectionSocket.close()

