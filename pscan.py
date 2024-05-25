import nmap

scanner = nmap.PortScanner()
while True:
    print("Seja bem vindo ao Scanner")
    print("<----------------------->")

    ip = input("Digite o ip a ser varriado: ")
    print("o ip digitado foi: ", ip)
    type(ip)

    menu = input(""""\n Escolha o tipo varredura a ser Realizada
                1 -> Varredura do Tipo SYN
                2 -> Varredura do Tipo UDP
                3 -> Varredura do Tipo Intensa
                Digite a opção escolhida: """)
    print("A opção escolhida foi", menu)

    if menu == "1":
        print("Versão do Nmap:", scanner.nmap_version())
        scanner.scan(ip, "1-1024", '-v -sS')
        print(scanner.scaninfo())
        print("Status do Ip: ", scanner[ip].state())
        print(scanner[ip].all_protocols())
        print("")
        print("Porta Abertas: ", scanner[ip]['tcp'].keys())

    elif menu == "2":
        print("Versão do Nmap:", scanner.nmap_version())
        scanner.scan(ip, "1-1024", '-v -sU')
        print(scanner.scaninfo())
        print("Status do Ip: ", scanner[ip].state())
        print(scanner[ip].all_protocols())
        print("")
        print("Portas Abertas: ", scanner[ip]["udp"].keys())
    elif menu == "3":
        print("Versão do Nmap", scanner.nmap_version())
        scanner.scan(ip, '1-1024', '-v -sC')
        print("Status do Ip: ", scanner[ip].state())
        print(scanner[ip].all_protocols())
        print("")
        print("Portas Abertas: ", scanner[ip]['tcp'].keys())
    else:
        print("Escolha uma opção corretar!!!")
        continue

    repetir = input("Realizar outro scanner? (y-sim / n-não): ")
    if repetir.lower() != "y":
        break