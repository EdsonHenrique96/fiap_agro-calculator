cafe = {
    "largura_rua": 2.5,
    "largura_fileira_plantas": 1,
    "espaco_entre_mudas": 0.8,
}

soja = {
    "largura_rua": 0.5,
    "largura_fileira_plantas": 1,
    "desidade": [20, 25, 30, 35, 40],
}

culturas = ["Café", "Soja"]


def mostrar_cultura_selecionada(cultura_selecionada: int):
    return culturas[cultura_selecionada - 1] if cultura_selecionada > 0 else ""


def get_cultura(cultura: str):
    if cultura == "cafe":
        return cafe
    else:
        return soja
