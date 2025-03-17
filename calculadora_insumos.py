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
        "calcario": calcario_total,
        "fertilizantes": fertilizantes_total,
        "agua": agua_total,
        "palhada": palhada_total,
        "mudas": mudas_total,
    }


__all__ = ["cal_insumos"]
