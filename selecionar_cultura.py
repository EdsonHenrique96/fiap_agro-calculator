from utils import delimiter, limpar


def selecionar_cultura():
    opcao_cultura = ""

    while True:
        limpar()
        print(delimiter)
        print("Selecione a cultura desejada:\n")
        print("1. Café")
        print("2. Soja")
        print(delimiter)
        opcao_cultura = int(input("\nDigite o número da cultura desejada: "))

        match opcao_cultura:
            case 1:
                print("Café selecionado")
                break
            case 2:
                print("Soja selecionada")
                break
            case _:
                print("\nOpção inválida! Informe uma opção válida de 1 a 2.")
                input("\nPressione Enter para continuar...")
                limpar()

    return opcao_cultura
