from utils import formatar_numero


def cal_insumos(area_util):
    espaco_entre_mudas = 0.8
    espaco_fileiras = 3.5
    calcario = 0.3
    fertilizantes = 0.15
    agua = 0.5
    palhada = 5

    calcario_total = calcario * area_util
    fertilizantes_total = fertilizantes * area_util
    agua_total = agua * area_util
    palhada_total = palhada * area_util

    mudas_por_m2 = espaco_entre_mudas * espaco_fileiras
    mudas_total = area_util / mudas_por_m2

    return {
        "Calcario": formatar_numero(calcario_total),
        "Fertilizantes": formatar_numero(fertilizantes_total),
        "Agua": formatar_numero(agua_total),
        "Palhada": formatar_numero(palhada_total),
        "Mudas": formatar_numero(mudas_total),
    }


__all__ = ["cal_insumos"]
