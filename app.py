estoque = []

def cadastrar_produto():
    nome = input("Digite o nome do produto para cadastrar: ")
    if nome:
        estoque.append(nome)
        print("Produto '" + nome + "' adicionado com sucesso.")
    else:
        print("Erro: Nome invalido.")

def remover_produto():
    nome = input("Digite o nome do produto para remover: ")
    if nome in estoque:
        estoque.remove(nome)
        print("Produto '" + nome + "' removido.")
    else:
        print("Erro: Produto nao encontrado.")

def listar_produtos():
    if not estoque:
        print("\nO estoque esta vazio.")
    else:
        print("\n--- Lista de Produtos ---")
        for i, produto in enumerate(estoque, 1):
            print(str(i) + ". " + produto)
        print("-------------------------")

def executar_sistema():
    print("--- Sistema de Gestao de Estoque ---")
    
    while True:
        print("\nMenu: 1 (Cadastrar) | 2 (Remover) | 3 (Listar) | 0 (Sair)")
        entrada = input("Escolha uma funcionalidade: ")

        try:
            opcao_int = int(entrada)
            
            match opcao_int:
                case 1:
                    cadastrar_produto()
                case 2:
                    remover_produto()
                case 3:
                    listar_produtos()
                case 0:
                    print("Encerrando execucao.")
                    break
                case _:
                    print("Opcao invalida.")
        except ValueError:
            print("Erro: Por favor, digite apenas numeros inteiros.")

if __name__ == "__main__":
    executar_sistema()
