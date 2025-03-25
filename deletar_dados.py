from utils import delimiter, limpar, confirmar_para_seguir


def deletar_dados(fazenda: list, dimensoes: list, cultura: int):

    while True:
        limpar()
        print(delimiter)
        print("Selecione o que deseja deletar: ")
        print("1. Fazenda")
        print("2. Voltar a menu principal")
        print(delimiter)
        opcao = int(input("\nDigite o número da cultura desejada: ") or 0)

        match opcao:
            case 1:
                while True:
                    print("\nRealmente deseja deletar todos os dados da fazenda ?")
                    prosseguir = input("\n [sim] para prosseguir, [nao] para voltar: ")

                    if prosseguir == "sim":
                        fazenda = []
                        dimensoes = [0, 0]
                        cultura = 0
                        limpar()
                        print("\nFazenda deletada com sucesso!!\n")
                        confirmar_para_seguir()
                        break
                    elif prosseguir == "nao":
                        break

                    print("\n***Opção inválida***\n")
            case 2:
                break
            case _:
                print("\nOpção inválida! Informe uma opção válida de 1 a 2.")
                confirmar_para_seguir()

    return {"fazenda": fazenda, "dimensoes": dimensoes, "cultura": cultura}
