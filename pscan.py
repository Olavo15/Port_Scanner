import nmap

def main():
    scanner = nmap.PortScanner()
    while True:
        print("Seja bem vindo ao Scanner")
        print("<----------------------->")

        ip = input("Digite o IP a ser varrido: ")
        print("O IP digitado foi:", ip)

        menu = input("""
Escolha o tipo de varredura a ser realizada:
                1 -> Varredura do Tipo SYN
                2 -> Varredura do Tipo UDP
                3 -> Varredura do Tipo Intensa
Digite a opção escolhida: """)
        print("A opção escolhida foi", menu)

        try:
            if menu == "1":
                print("Versão do Nmap:", scanner.nmap_version())
                scanner.scan(ip, "1-1024", '-v -sS')
                print(scanner.scaninfo())
                print("Status do IP:", scanner[ip].state())
                print(scanner[ip].all_protocols())
                print("Portas Abertas:", scanner[ip]['tcp'].keys())

            elif menu == "2":
                print("Versão do Nmap:", scanner.nmap_version())
                scanner.scan(ip, "1-1024", '-v -sU')
                print(scanner.scaninfo())
                print("Status do IP:", scanner[ip].state())
                print(scanner[ip].all_protocols())
                print("Portas Abertas:", scanner[ip]['udp'].keys())

            elif menu == "3":
                print("Versão do Nmap:", scanner.nmap_version())
                scanner.scan(ip, '1-1024', '-v -sC')
                print("Status do IP:", scanner[ip].state())
                print(scanner[ip].all_protocols())
                print("Portas Abertas:", scanner[ip]['tcp'].keys())

            else:
                print("Escolha uma opção correta!!!")
                continue

        except nmap.PortScannerError as e:
            print(f"Erro ao executar o scanner: {e}")
            print("Verifique se você tem as permissões necessárias (root) para executar esta varredura.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        repetir = input("Realizar outro scanner? (y-sim / n-não): ")
        if repetir.lower() != "y":
            break

if __name__ == "__main__":
    main()
