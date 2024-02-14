def ler_ficheiro(idade, modalidade, resultado):
    ficheiro = open("emd.csv")
    ficheiro.readline() 
    for linha in ficheiro:
        campos = linha.split(",")
        idade.append(int(campos[5]))
        modalidade.append(campos[8])
        resultado.append(campos[12].rstrip())  # retirar a new line
    ficheiro.close()


def modalidades_ordenadas(modalidade):
    ordenado = sorted(set(modalidade))
    print("\n----- Aqui estão as modalidades ordenadas: -----\n")
    for mod in ordenado:
        print(f"- {mod}")


def percentagem_aptos(resultado):
    aptos = resultado.count('true') / len(resultado) * 100
    inaptos = 100 - aptos
    print("\n----- Percentagem de atletas aptos e inaptos para a prática desportiva. -----\n")
    print(f"{aptos:.2f}% dos atletas estão aptos e {inaptos:.2f}% dos atletas estão inaptos para a prática desportiva.")


def distribuicao_idades(idade):
    distribuicao = {}
    for i in range(len(idade)):
        decisao = (idade[i] // 5) * 5
        if decisao in distribuicao:
            distribuicao[decisao] +=1
        else:
            distribuicao.update({decisao: 1})

    ordem = dict(sorted(distribuicao.items()))

    print("\nDistribuição dos atletas pela faixa etária: ")
    print(">----------------|--------------<")
    print(">-[Faixa etária]-|-[Nº Atletas]-<")
    print(">----------------|--------------<")
    for key, valor in ordem.items():
        if valor < 10:
            print(f">    [{key},{key + 4}]     |      {valor}       <")
        elif valor < 100:
            print(f">    [{key},{key + 4}]     |      {valor}      <")
        else:
            print(f">    [{key},{key + 4}]     |      {valor}     <")
    print(">----------------|--------------<")


def main():
    idade = []
    modalidade = []
    resultado = []
    ler_ficheiro(idade, modalidade, resultado)

    print("O que pretende obter? ")
    print("1. Lista das modalidades ordenada alfabeticamente.\n"
          "2. Percentagem de atletas aptos e inaptos para a prática desportiva.\n"
          "3. Distribuição de atletas por escalão etário.\n"
          "0. Sair.")
    opcao = int(input("\nEscolha: "))

    while opcao != 0:
        if opcao == 1:
            modalidades_ordenadas(modalidade)
        elif opcao == 2:
            percentagem_aptos(resultado)
        elif opcao == 3:
            distribuicao_idades(idade)
        else:
            print("O valor que introduziu não é aceite. Tente outra vez.")
        opcao = int(input("\nEscolha: "))


if __name__ == "__main__":
    main()
