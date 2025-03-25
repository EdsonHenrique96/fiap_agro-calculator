import math

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
