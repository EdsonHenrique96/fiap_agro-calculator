# Entrada de dados (entrada dos dados para realizar os cálculos);
# Saída de dados (como impressões de dados no terminal);
# Atualização de dados numa posição qualquer do vetor;
# Deleção de dados do vetor de dados;
# Ter a opção “sair do programa”;
from utils import delimiter, limpar
from calculadora_area import (
    show_calculadora_area_description,
    get_largura,
    get_comprimento,
    calc_area_total,
    calc_hectares,
    calc_quantidade_fileiras,
    calc_area_util_de_plantio,
)
from calculadora_insumos import cal_insumos
from selecionar_cultura import selecionar_cultura
from utils import formatar_numero


def menu():
    running = True
    largura = 0
    comprimento = 0
    area = 0
    area_total_hectares = 0
    cultura_selecionada = 0
    num_fileiras = 0
    area_util = 0
    insumos = {}

    while running:
        print(f"Cultura selecionada: {cultura_selecionada}\n")
        print("Terreno:")
        print(
            f"""
            Largura ({formatar_numero(largura)}m)
             _________
            |         |   
            |    A    | Comprimento ({formatar_numero(comprimento)}m)
            |_________|
            """
        )
        print(f"Area: {area}m²\n")
        print(f"Hectares: {area_total_hectares}\n")

        print(delimiter)
        print("Escolha uma opção:\n")
        print("1. Entrada de dados")
        print("2. Saída de dados")
        print("3. Atualização de dados")
        print("4. Deleção de dados")
        print("5. Sair do programa")
        print(delimiter)
        opcao = int(input("Digite o número da opção desejada: "))

        match opcao:
            case 1:
                limpar()
                show_calculadora_area_description()
                largura = get_largura()
                comprimento = get_comprimento()

                area = calc_area_total(largura, comprimento)
                area_total_hectares = calc_hectares(area)

                print(delimiter)
                print(
                    f"A área do terreno é de {area} m², que equivale a {area_total_hectares} hectares"
                )
                print("\n")
                input("Pressione Enter para continuar...")

                limpar()
                cultura_selecionada = selecionar_cultura()

                if cultura_selecionada == 1:
                    limpar()
                    print("Calculando insumos para café...")
                    num_fileiras = calc_quantidade_fileiras(largura)
                    area_util = calc_area_util_de_plantio(
                        area, num_fileiras, comprimento
                    )
                    insumos = cal_insumos(area_util)
                    print("\n")
                    input("Pressione Enter para continuar...")
                    limpar()
                elif cultura_selecionada == 2:
                    limpar()
                    print("Calcular insumos para soja...")

            case 2:
                limpar()
                print(delimiter)
                print("Informações do terreno:\n")
                print(f"Numero de fileiras: {formatar_numero(num_fileiras)}")
                print(f"Area útil de plantio: {formatar_numero(area_util)} m²")
                print(delimiter)
                print("Insumos:\n")
                for key, value in insumos.items():
                    print(f"{key}: {value}")
                print(delimiter)
                print("\n")
                input("Pressione Enter para continuar...")
                limpar()
            case 3:
                limpar()
                print("Atualização de dados")
            case 4:
                limpar()
                print("Deleção de dados")
            case 5:
                print("Saindo do programa...")
                break
            case _:
                print("Opção inválida! Informe uma opção válida de 1 a 5.")
