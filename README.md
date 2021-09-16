# Port Scanner TCP

A aplicação consiste num scanner que, dado um host alvo e um intervalo de portas, analisa quais delas estão abertas, filtradas ou fechadas. 
Desenvolvida em Python 3.6.9 e fazendo uso da API de sockets da dita linguagem.

Desenvolvido por Luam Souza, Victória Granja, Lucas Fauster e Juliana Moura para a disciplina de Redes de Computadores.

O algoritmo consiste em um laço de repetição que testa, porta a porta, se a conexão à esta é bem sucedida (ou seja, porta aberta),
do contrário faz-se uso de exceções da API de sockets para capturar àquelas portas que são filtradas ou fechadas.
A maneira pela qual o grupo otimizou a identificação de portas filtradas foi através do método ".settimeout", 
que define o tempo máximo pelo qual o socket deverá aguardar conexão. O valor padrão de time out adotado foi 1s,
mas este poder melhor calibrado dependendo do servidor.

# Execução
Para executar a aplicação basta rodar em um terminal python `TCP-cliente-socket.py` e digitar os respetivos host e intervalo de portas. 
Se desejar usar um host local, pode-se executar também o `TCP-servidor-socket.py` (antes de subir o dito cliente).

# Exemplos

```
Port Scanner TCP
-----------------------------
Digite o hostname ou o endereço IP do server alvo: localhost
Digite um intervalo de portas para chegar (ex. 1000 e 2000):
Porta inicial: 11990
Porta final: 12005

Portas
-----------------------------
Abertas: [12000]
Filtradas: []
Fechadas: [11990, 11991, 11992, 11993, 11994, 11995, 11996, 11997, 11998, 11999, 12001, 12002, 12003, 12004, 12005]
```
```
Port Scanner TCP
-----------------------------
Digite o hostname ou o endereço IP do host alvo: www.google.com
Digite um intervalo de portas para chegar (ex. 1000 e 2000):
Porta inicial: 78
Porta final: 82

Portas
-----------------------------
Abertas: [80]
Filtradas: [78, 79, 81, 82]
Fechadas: []
```
