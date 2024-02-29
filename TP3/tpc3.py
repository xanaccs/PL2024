import re

def somador(input):
    contador = 0
    estado = False
    resultados = []

    # Adicionar todos os On/Off/=/números numa lista
    lista_final = re.findall(r'(on|off|=|\d+)', input, re.IGNORECASE)

    for elemento in lista_final:
        if elemento.lower() == "=":
            resultados.append(f"Soma = {contador}")
            contador = 0
        elif elemento.isdigit() and estado:
            contador += int(elemento)
        elif elemento.upper() == "OFF":
            estado = False
        elif elemento.upper() == "ON":
            estado = True
    
    resultados.append(f"Soma = {contador}")
    return resultados

if __name__ == "__main__":
    with open("exemplo.txt", "r") as ficheiro:
        input = ficheiro.read()

    resultados = somador(input)

    for resultado in resultados:
        print(resultado)