from utils import formatar_numero
from constantes import get_cultura


def cal_insumos_soja(area_util, densidade):
    calcario = 0.1  # kg/m² (convertido de 100g)
    gesso = 0.05  # kg/m² (convertido de 50g)
    fosfato = 0.002  # kg/m² (convertido de 2g)
    potassio = 0.002  # kg/m² (convertido de 2g)
    nitrogenio = 0  # kg/m² (convertido de 0g)
    herbicida = 0.01  # mL/m²
    fungicida = 0.01  # mL/m²
    inseticida = 0.005  # mL/m²
    agua = 4  # L/m²/dia

    return {
        "Calcário": f"{formatar_numero(calcario * area_util)} Kg",
        "Gesso": f"{formatar_numero(gesso * area_util)} Kg",
        "Fosfato": f"{formatar_numero(fosfato * area_util)} Kg",
        "Potássio": f"{formatar_numero(potassio * area_util)} Kg",
        "Nitrogênio": f"{formatar_numero(nitrogenio * area_util)} Kg",
        "Herbicida": f"{formatar_numero(herbicida * area_util)} mL",
        "Fungicida": f"{formatar_numero(fungicida * area_util)} mL",
        "Inseticida": f"{formatar_numero(inseticida * area_util)} mL",
        "Água": f"{formatar_numero(agua * area_util)} L por dia",
    }


def cal_total_mudas_cafe(area_total):
    cafe = get_cultura("cafe")
    largura_rua = cafe["largura_rua"]
    largura_fileira_plantas = cafe["largura_fileira_plantas"]
    espaco_entre_mudas = cafe["espaco_entre_mudas"]

    mudas_por_metro_quadrado = (
        largura_rua + largura_fileira_plantas
    ) * espaco_entre_mudas

    return round(area_total / round(mudas_por_metro_quadrado, 1), 2)


def cal_insumos_cafe(area_util, area_total):
    mudas = cal_total_mudas_cafe(area_total)
    nitrogenio = 0.002  # kg/m² (convertido de 2g)
    fosforo = 0.001  # kg/m² (convertido de 1g)
    potassio = 0.002  # kg/m² (convertido de 2g)
    calcario = 0.2  # kg/m² (convertido de 200g)
    gesso = 0.1  # kg/m² (convertido de 100g)
    herbicida = 0.01  # mL/m²
    fungicida = 0.01  # mL/m²
    inseticida = 0.005  # mL/m²
    agua = 6  # L/m²/dia

    return {
        "Mudas": f"{formatar_numero(mudas)} mudas",
        "Nitrogênio": f"{formatar_numero(nitrogenio * area_util)} Kg",
        "Fósforo": f"{formatar_numero(fosforo * area_util)} Kg",
        "Potássio": f"{formatar_numero(potassio * area_util)} Kg",
        "Calcário": f"{formatar_numero(calcario * area_util)} Kg",
        "Gesso Agrícola": f"{formatar_numero(gesso * area_util)} Kg",
        "Herbicida": f"{formatar_numero(herbicida * area_util)} mL",
        "Fungicida": f"{formatar_numero(fungicida * area_util)} mL",
        "Inseticida": f"{formatar_numero(inseticida * area_util)} mL",
        "Água": f"{formatar_numero(agua * area_util)} L por dia",
    }
