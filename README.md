# Scanner de Portas com Nmap

Este é um simples script em Python que utiliza a biblioteca Nmap para realizar varreduras de portas em um determinado IP. Ele permite que você escolha o tipo de varredura desejada e exibe as portas abertas.

## Como usar

1. Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

2. Instale a biblioteca Nmap utilizando o seguinte comando pip:
    ```
    pip install python-nmap
    ```

3. Clone este repositório para sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/scanner-de-portas.git
    ```

4. Navegue até o diretório do projeto:
    ```bash
    cd scanner-de-portas
    ```

5. Execute o script Python usando o seguinte comando:
    ```bash
    python scanner.py
    ```

6. Siga as instruções exibidas no console para inserir o IP que deseja varrer e escolher o tipo de varredura (SYN, UDP ou Intensa).

7. O resultado da varredura será exibido no console, mostrando as portas abertas.

8. Você terá a opção de realizar outra varredura ou sair do programa.
