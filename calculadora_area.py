import math
from utils import delimiter, limpar
from constantes import get_cultura


# Em casos que o numero de ruas é quebrado, arredondar para baixo
def calc_quantidade_fileiras(largura_terreno: float, cultura: str = "cafe"):
    cultura = get_cultura(cultura)
    largura_fileira_total = cultura["largura_rua"] + cultura["largura_fileira_plantas"]
    return math.floor(largura_terreno / largura_fileira_total)


def calc_area_util_de_plantio(
    area_total, qtd_fileiras, comprimento_terreno, cultura: str = "cafe"
):
    cultura = get_cultura(cultura)
    total_area_rua = qtd_fileiras * cultura["largura_rua"] * comprimento_terreno
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


def get_densidade():
    densidade = 0

    while True:
        print(delimiter)
        print("Densidade de plantio:")
        print("1. 20 plantas/m²")
        print("2. 25 plantas/m²")
        print("3. 30 plantas/m²")
        print("4. 35 plantas/m²")
        print("5. 40 plantas/m²")
        print(delimiter)
        densidade = int(input("Escolha a densidade de plantio: "))

        match densidade:
            case 1:
                densidade = 20
                break
            case 2:
                densidade = 25
                break
            case 3:
                densidade = 30
                break
            case 4:
                densidade = 35
                break
            case 5:
                densidade = 40
                break
            case _:
                print("\nOpção inválida! Informe uma opção válida de 1 a 5.")
                input("\nPressione Enter para continuar...")
                limpar()

    return densidade
