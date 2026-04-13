produtos = []

def listarprodutos():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        for i in range(len(produtos)):
            print(f"{i} - Nome: {produtos[i]['nome']} | Preço: {produtos[i]['preco']}")
    return produtos


def adicionarproduto(produto):
    produtos.append(produto)
    return True


def buscarproduto(nome):
    for i in range(len(produtos)):
        if produtos[i]["nome"] == nome:
            return i
    return None


def atualizarproduto(indice, novoproduto):
    produtos[indice] = novoproduto
    return True


def removerproduto(indice):
    produtos.pop(indice)
    return True


opcao = -1

while opcao != 0:
    print("\n===== MENU =====")
    print("1 - Listar Produtos")
    print("2 - Adicionar Produto")
    print("3 - Buscar Produto")
    print("4 - Atualizar Produto")
    print("5 - Remover Produto")
    print("0 - Sair")
    
    opcao = int(input("Escolha uma opcao: "))
    
    if opcao == 1:
        listarprodutos()

    elif opcao == 2:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preco do produto: "))
        produto = {"nome": nome, "preco": preco}

        if adicionarproduto(produto):
            print("Produto cadastrado com sucesso!")

    elif opcao == 3:
        nome = input("Digite o nome do produto: ")
        indice = buscarproduto(nome)

        if indice is not None:
            print(f"Produto encontrado no índice {indice}")
        else:
            print("Produto não encontrado.")

    elif opcao == 4:
        indice = int(input("Digite o índice do produto: "))
        nome = input("Novo nome: ")
        preco = float(input("Novo preço: "))

        novoproduto = {"nome": nome, "preco": preco}

        if atualizarproduto(indice, novoproduto):
            print("Produto atualizado com sucesso!")

    elif opcao == 5:
        indice = int(input("Digite o índice do produto: "))

        if removerproduto(indice):
            print("Produto removido com sucesso!")

    elif opcao == 0:
        print("Encerrando sistema...")

    else:
        print("Opção inválida!")
