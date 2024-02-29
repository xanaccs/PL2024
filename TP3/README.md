# TP3 : Somador on/off 

## Alexandra Santos, a94523

Para este tpc, foi criado um programa que lê um ficheiro de texto chamado "exemplo.txt" que contem uma sequência de comandos e numeros.

O programa percorre a lista de comandos e números extraídos e realiza as seguintes ações:

* Soma todas as sequências de dígitos que encontrar num texto; 
* Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
* Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
* Se o elemento for "=", adiciona a mensagem "Total atual: " seguida do valor atual do contador à lista de resultados.
* Se o elemento for um número e o estado for "on", adiciona o valor do número ao contador.
