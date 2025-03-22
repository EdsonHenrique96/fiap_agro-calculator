from utils import delimiter


def get_largura():
    while True:
        largura = input("Digite a largura do terreno em metros: ")

        if not largura.isnumeric():
            print("\n***Valor inválido, digite um valor númerico!***\n")
            continue
        elif float(largura) <= 0:
            print("\n***Valor deve ser maior que zero!***\n")
            continue
        else:
            break

    return float(largura)


def get_comprimento():
    while True:
        comprimento = input("Digite o comprimento do terreno em metros: ")

        if not comprimento.isnumeric():
            print("\n***Valor inválido, digite um valor númerico!***\n")
            continue
        elif float(comprimento) <= 0:
            print("\n***Valor deve ser maior que zero!***\n")
            continue
        else:
            break

    return float(comprimento)


def form_dimensoes(dimensoes: list):
    print("Dimensões do terreno:\n")
    dimensoes[0] = get_largura()
    dimensoes[1] = get_comprimento()
    print(delimiter)
