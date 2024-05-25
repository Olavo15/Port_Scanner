import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

ip = input("Digite o host ou ip a ser Verificado: ")
port = int(input("Digite a porta a ser Verificada: "))

code = client.connect_ex((ip, port))


if code == 0:
    print("Porta Aberta")
else:
    print("Porta Fechada")
