import math
from utils import delimiter
from insumos_calculator import cal_insumos

largura_rua = 2.5
largura_fileira_plantas = 1


# Em casos que o numero de ruas é quebrado, arredondar para baixo
def calc_quantidade_fileiras(largura_terreno, largura_rua, largura_fileira_plantas):
    largura_fileira_total = largura_rua + largura_fileira_plantas
    return math.floor(largura_terreno / largura_fileira_total)


def calc_area_util_de_plantio(
    area_total, qtd_fileiras, largura_rua, comprimento_terreno
):
    total_area_rua = qtd_fileiras * largura_rua * comprimento_terreno
    return area_total - total_area_rua


def calc_hectares(area):
    return area / 10000


def calc_area(length, width):
    return length * width


def calc_area_total(largura, comprimento):
    area_total = largura * comprimento

    return area_total


def area_calculator():
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
    largura = float(input("Digite a largura do terreno em metros: "))
    comprimento = float(input("Digite o comprimento do terreno em metros: "))
    print(delimiter)
    area = calc_area_total(largura, comprimento)
    area_total_hectares = calc_hectares(area)
    num_fileiras = calc_quantidade_fileiras(
        largura, largura_rua, largura_fileira_plantas
    )
    area_util = calc_area_util_de_plantio(area, num_fileiras, largura_rua, comprimento)
    print(
        f"A área do terreno é de {area} m², que equivale a {area_total_hectares} hectares"
    )
    print(f"Numero de fileiras: {num_fileiras}")
    print(f"Area util de plantio: {area_util}")
    print(cal_insumos(area_util))
    print("\n\n")


area_calculator()
