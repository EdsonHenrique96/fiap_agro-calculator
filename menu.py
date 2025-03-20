# Entrada de dados (entrada dos dados para realizar os cálculos);
# Saída de dados (como impressões de dados no terminal);
# Atualização de dados numa posição qualquer do vetor;
# Deleção de dados do vetor de dados;
# Ter a opção “sair do programa”;
from utils import delimiter, limpar
from calculadora_area import (
    show_cadastro_fazenda_descricao,
    calc_area_total,
    calc_hectares,
    calc_quantidade_fileiras,
    calc_area_util_de_plantio,
    get_densidade,
)
from form_dados_cadastrais import form_dados_cadastrais
from form_dimensoes import form_dimensoes
from calculadora_insumos import cal_insumos_cafe, cal_insumos_soja
from selecionar_cultura import selecionar_cultura
from utils import formatar_numero
from constantes import culturas
from atualizar_dados import menu_atualizar_dados


def menu():
    running = True
    area = 0
    area_total_hectares = 0
    cultura_selecionada = 0
    num_fileiras = 0
    area_util = 0
    densidade = 0
    insumos = {}

    # nome, rua, numero, bairro, cidade, estado, cep, proprietario, telefone, email
    fazenda = []

    # largura, comprimento
    dimensoes = [0, 0]

    while running:
        print(f"Cultura selecionada: {culturas[cultura_selecionada-1]}\n")
        print("Terreno:")
        print(
            f"""
            Largura ({formatar_numero(dimensoes[0])}m)
             _________
            |         |   
            |    A    | Comprimento ({formatar_numero(dimensoes[1])}m)
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
        opcao = int(input("Digite o número da opção desejada: ") or 0)

        match opcao:
            case 1:
                limpar()
                print(delimiter)
                show_cadastro_fazenda_descricao()
                form_dados_cadastrais(fazenda)
                form_dimensoes(dimensoes)

                area = calc_area_total(dimensoes[0], dimensoes[1])
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
                    num_fileiras = calc_quantidade_fileiras(dimensoes[0])
                    area_util = calc_area_util_de_plantio(
                        area, num_fileiras, dimensoes[1]
                    )
                    insumos = cal_insumos_cafe(area_util=area_util, area_total=area)
                    print("\n")
                    input("Pressione Enter para continuar...")
                    limpar()
                elif cultura_selecionada == 2:
                    limpar()
                    densidade = get_densidade()
                    limpar()
                    print("Calcular insumos para soja...")
                    num_fileiras = calc_quantidade_fileiras(
                        largura_terreno=dimensoes[0], cultura="soja"
                    )
                    area_util = calc_area_util_de_plantio(
                        area, num_fileiras, dimensoes[1], cultura="soja"
                    )
                    insumos = cal_insumos_soja(area_util=area_util, densidade=densidade)
                    print("\n")
                    input("Pressione Enter para continuar...")
                    limpar()

            case 2:
                limpar()
                print(delimiter)
                print("Informações da fazenda:\n")
                for item in fazenda:
                    print(f"{item[0]}: {item[1]}")
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
                menu_atualizar_dados(fazenda=fazenda, dimensoes=dimensoes)
                limpar()
            case 4:
                limpar()
                print("Deleção de dados")
            case 5:
                print("Saindo do programa...")
                break
            case _:
                print("\nOpção inválida! Informe uma opção válida de 1 a 5.")
                input("\nPressione Enter para continuar...")
                limpar()
