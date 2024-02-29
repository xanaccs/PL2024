# TP3 : Somador on/off 

## Alexandra Santos, a94523

Para este tpc, foi criado um programa que lê um ficheiro de texto chamado "exemplo.txt" que contem uma sequência de comandos e numeros.

O programa percorre a lista de comandos e números extraídos e realiza as seguintes ações:

Se o elemento for "on", define o estado como "on".
Se o elemento for "off", define o estado como "off".
Se o elemento for "=", adiciona a mensagem "Total atual: " seguida do valor atual do contador à lista de resultados.
Se o elemento for um número e o estado for "on", adiciona o valor do número ao contador.

# Execução
Para executar o programa:
$ cat exemplo.txt | python3 tpc3.py
