cafe = {
    "largura_rua": 2.5,
    "largura_fileira_plantas": 1,
    "espaco_entre_mudas": 0.8,
}

soja = {
    "largura_rua": 0.5,
    "largura_fileira_plantas": 0.5,
    "desidade": [20, 25, 30, 35, 40],
}


def get_cultura(cultura: str):
    if cultura == "cafe":
        return cafe
    else:
        return soja
