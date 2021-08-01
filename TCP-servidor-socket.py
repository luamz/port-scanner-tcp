from socket import *

# Porta que o servidor espera conexoes.
portaServidor = 12000

# Cria o socket. AF_INET e SOCK_STREAM indicam TCP.
socketServidor = socket(AF_INET, SOCK_STREAM)

# Associar o socket a porta
socketServidor.bind(('', portaServidor))

socketServidor.listen(1)

# Loop infinito: servidor eh capaz de tratar multiplas conexoes
while 1:

    # Aguardar nova conexao
    print 'Aguardando conexao...'
    connectionSocket, addr = socketServidor.accept()
    print 'Nova conexao recebida!'

    # Fechamento
    print 'Fechando socket...'
    connectionSocket.close()