from utils import delimiter


def get_largura():
    largura = float(input("Digite a largura do terreno em metros: "))
    return largura


def get_comprimento():
    comprimento = float(input("Digite o comprimento do terreno em metros: "))
    return comprimento


def form_dimensoes(dimensoes: list):
    print("Dimensões do terreno:\n")
    dimensoes[0] = get_largura()
    dimensoes[1] = get_comprimento()
    print(delimiter)
