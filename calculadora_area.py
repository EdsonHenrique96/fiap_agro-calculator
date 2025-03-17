import math
from utils import delimiter
from calculadora_insumos import cal_insumos

largura_rua = 2.5
largura_fileira_plantas = 1


# Em casos que o numero de ruas é quebrado, arredondar para baixo
def calc_quantidade_fileiras(largura_terreno):
    largura_fileira_total = largura_rua + largura_fileira_plantas
    return math.floor(largura_terreno / largura_fileira_total)


def calc_area_util_de_plantio(area_total, qtd_fileiras, comprimento_terreno):
    total_area_rua = qtd_fileiras * largura_rua * comprimento_terreno
    return area_total - total_area_rua


def calc_hectares(area):
    return area / 10000


def calc_area(length, width):
    return length * width


def calc_area_total(largura, comprimento):
    area_total = largura * comprimento

    return area_total


def show_calculadora_area_description():
    print(delimiter)
    print("Calculadora de área (A)\n")
    print(
        """
        Largura (Metros)
        _________
       |         |   
       |    A    | Comprimento (Metros)
       |_________|
    """
    )
    print(delimiter)


def get_largura():
    largura = float(input("Digite a largura do terreno em metros: "))

    return largura


def get_comprimento():
    comprimento = float(input("Digite o comprimento do terreno em metros: "))

    return comprimento


def calculadora_area():

    print(delimiter)
