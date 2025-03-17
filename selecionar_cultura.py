from utils import delimiter, limpar


def selecionar_cultura():
    opcao_cultura = 0

    while True:
        print(delimiter)
        print("Selecione a cultura desejada:\n")
        print("1. Café")
        print("2. Soja")
        print("3. Voltar ao menu principal")
        print(delimiter)
        opcao_cultura = int(input("\nDigite o número da cultura desejada: "))

        match opcao_cultura:
            case 1:
                print("Café selecionado")
                break
            case 2:
                print("Soja selecionada")
                break
            case 3:
                limpar()
                break
            case _:
                print("Opção inválida! Informe uma opção válida de 1 a 2.")

    return opcao_cultura
