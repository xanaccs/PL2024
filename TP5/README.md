# TPC5: Vending Machine

## Alexandra Santos, a94523


Este programa simula o comportamento de uma máquina de vendas.
O programa é implementado em Python e define várias funções para executar as diferentes operações suportadas pela máquina de vendas, como listar produtos, adicionar moedas, selecionar produtos para compra, adicionar produtos e sair do sistema.
Além disso, o programa armazena os dados do stock em um arquivo JSON, permitindo que os dados sejam facilmente armazenados e recuperados.

A lógica principal do programa está definida na função main(), onde o utilizador é solicitado a introduzir comandos até que ele deseje sair do sistema. Em seguida, a função processar_comando() é chamada para processar o comando fornecido pelo utilizador e executar a operação correspondente. 

Dependendo do comando introduzido pelo utilizador, o programa executa a operação correspondente e retorna o resultado. Os comandos disponíveis são:
* LISTAR: Lista todos os produtos disponíveis.
* MOEDA: Adiciona a quantidade especificada de moedas, atualizando o saldo atual.
* SELECIONAR: Permite ao utilizador selecionar um produto para comprar, verificando se o produto existe e se há quantidade disponível para a venda.
* ADICIONAR: Adiciona novos produtos à máquina, podendo ser produtos que já existem ou novos produtos.
* SAIR: Finalizar as transações, guardando o estado atual do stock após o uso.