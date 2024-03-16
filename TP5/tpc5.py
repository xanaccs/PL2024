import re
import json

# Carregar o stock a partir do ficheiro JSON
def carregar_stock(ficheiro):
    with open(ficheiro, 'r') as f:
        stock = json.load(f)
    print("maq: 2024-03-08, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    return stock['stock']

# Atualizar o stock e guarda-lo 
def atualizar_stock(ficheiro, stock):
  with open(ficheiro, 'w') as f:
    json.dump(stock, f)

# Menu da máquina
def apresentar_menu(stock):
  print("maq:")
  print("cod    |  nome      |  quantidade  |  preço")
  print("---------------------------------")
  for item in stock:
    print(f"{item['cod']}: {item['nome']}, {item['quant']}, {item['preco']}")

# Ccomando LISTAR os produtos
def listar_produtos(stock):
  apresentar_menu(stock)

# Comando MOEDA
def adicionar_moeda(moedas, saldo):
    for moeda in moedas:
        valor_moeda = re.findall(r'\d+', moeda)
        if valor_moeda:
            valor = int(valor_moeda[0])
            if "e" in moeda:
                saldo += valor * 100
            elif "c" in moeda:
                saldo += valor
            else:
                print(f"Moeda inválida: {moeda}")
                return saldo
    euros = saldo // 100
    cents = saldo % 100
    print(f"maq: Saldo = {euros}e{cents:02d}c")
    return saldo

# Comando SELECIONAR
def selecionar(stock, cod, saldo):
  item = next((item for item in stock if item['cod'] == cod), None)
  if item is None:
    print(f"maq: Produto inexistente: {cod}")
    return saldo
  if item['quant'] == 0:
    print(f"maq: Produto esgotado: {cod}")
    return saldo
  if saldo < item['preco']:
    print(f"maq: Saldo insuficiente")
    print(f"maq: Saldo = {saldo//100}e{saldo%10:02d}c; Pedido = {item['preco']}c")
    return saldo
  item['quant'] -= 1
  saldo -= item['preco']
  print(f"maq: Pode retirar o produto \"{item['nome']}\"")
  print(f"maq: Saldo = {saldo//100}e{saldo%100}c")
  return saldo

# Comando para adicionar novo produto
def adicionar_produto(stock):
    cod = input("Digite o código do novo produto: ")
    nome = input("Digite o nome do novo produto: ")
    quant = int(input("Digite a quantidade do novo produto: "))
    preco = float(input("Digite o preço do novo produto: "))
    novo_produto = {'cod': cod, 'nome': nome, 'quant': quant, 'preco': preco}
    stock.append(novo_produto)
    print(f"maq: Novo produto adicionado: {nome}, {quant}, {preco}")

# Comando SAIR
def sair(saldo):
  if saldo > 0:
    troco = []
    while saldo >= 50:
      troco.append("50c")
      saldo -= 50
    while saldo >= 20:
      troco.append("20c")
      saldo -= 20
    while saldo >= 10:
      troco.append("10c")
      saldo -= 10
    while saldo >= 5:
      troco.append("5c")
      saldo -= 5
    while saldo >= 2:
      troco.append("2c")
      saldo -= 2
    print(f"maq: Pode retirar o troco: {', '.join(troco)}")
  print("maq: Até à próxima")

# Função principal
def main():
  stock = carregar_stock("stock.json")
  saldo = 0
  while True:
    comando = input(">> ").strip().upper()
    if comando == "LISTAR":
      listar_produtos(stock)
    elif comando.startswith("MOEDA"):
      moedas = re.findall(r'\d+[ce]', comando)
      saldo = adicionar_moeda(moedas, saldo)
    elif comando.startswith("SELECIONAR"):
      cod = comando[11:].strip()
      saldo = selecionar(stock, cod, saldo)
    elif comando.startswith("ADICIONAR"):
       adicionar_produto(stock)
    elif comando == "SAIR":
      break
    else:
      print("maq: Comando inválido.")

  sair(saldo)

if __name__ == '__main__':
  main()

