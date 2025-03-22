from utils import delimiter, limpar, confirmar_para_seguir
from form_dados_cadastrais import (
    get_nome,
    get_rua,
    get_numero,
    get_bairro,
    get_cidade,
    get_estado,
    get_cep,
    get_proprietario,
    get_telefone,
    get_email,
)
from calculadora_area import (
    calc_area_total,
    calc_quantidade_fileiras,
    calc_area_util_de_plantio,
    get_densidade,
)
from calculadora_insumos import cal_insumos_cafe, cal_insumos_soja
from form_dimensoes import get_comprimento, get_largura


def atualizar_dimensoes_terreno(dimensoes: list):
    while True:
        limpar()
        print(delimiter)
        print("\nDimensões do terreno: \n")
        print(f"1. Largura - {dimensoes[0]}")
        print(f"2. Comprimento - {dimensoes[1]}")
        print("3. Voltar ao menu principal")
        print(delimiter)

        opcao = int(input("\nDigite o número da opção desejada: ") or 0)

        match opcao:
            case 1:
                dimensoes[0] = get_largura()
            case 2:
                dimensoes[1] = get_comprimento()
            case 3:
                limpar()
                break
            case _:
                print("\nOpção inválida! Informe uma opção válida de 100 a 200.")
                confirmar_para_seguir()

    return dimensoes


def menu_atualizar_dados_cadastrais(fazenda: list):
    while True:
        limpar()
        print(delimiter)
        print("\nDados cadastrais da fazenda: \n")
        for i, item in enumerate(fazenda, start=1):
            print(f"{i}. {item[0]} - {item[1]}")
        print("11. Voltar ao menu principal")
        print(delimiter)

        opcao = int(input("\nDigite o número do dado que deseja atualizar: ") or 0)

        match opcao:
            case 1:
                fazenda[0][1] = get_nome()
            case 2:
                fazenda[0][1] = get_rua()
            case 3:
                fazenda[0][1] = get_numero()
            case 4:
                fazenda[0][1] = get_bairro()
            case 5:
                fazenda[0][1] = get_cidade()
            case 6:
                fazenda[1][1] = get_estado()
            case 7:
                fazenda[2][1] = get_cep()
            case 8:
                fazenda[3][1] = get_proprietario()
            case 9:
                fazenda[4][1] = get_telefone()
            case 10:
                fazenda[5][1] = get_email()
            case 11:
                limpar()
                break
            case _:
                print("\nOpção inválida! Informe uma opção válida de 1 a 11.")
                confirmar_para_seguir()

    return fazenda


def menu_atualizar_dados(
    fazenda: list,
    dimensoes: list,
    cultura: int,
    insumos: dict,
):
    while True:
        limpar()
        print(delimiter)
        print("\nMenu de atualização de dados:\n")
        print("1. Dados cadastrais da fazenda")
        print("2. Dimensões do terreno")
        print("3. Voltar ao menu principal")
        print(delimiter)

        opcao = int(input("\nDigite o número da opção desejada: ") or 0)

        match opcao:
            case 1:
                menu_atualizar_dados_cadastrais(fazenda)
                break
            case 2:
                atualizar_dimensoes_terreno(dimensoes)

                area = calc_area_total(dimensoes[0], dimensoes[1])

                if cultura == 1:
                    print("\nAtualizando insumos para café...")
                    num_fileiras = calc_quantidade_fileiras(dimensoes[0])
                    area_util = calc_area_util_de_plantio(
                        area, num_fileiras, dimensoes[1]
                    )
                    insumos = cal_insumos_cafe(area_util=area_util, area_total=area)

                    confirmar_para_seguir()
                elif cultura == 2:
                    densidade = get_densidade()
                    print("\nAtualizando insumos para soja...")
                    num_fileiras = calc_quantidade_fileiras(
                        largura_terreno=dimensoes[0], cultura="soja"
                    )
                    area_util = calc_area_util_de_plantio(
                        area, num_fileiras, dimensoes[1], cultura="soja"
                    )
                    cal_insumos_soja(area_util=area_util, densidade=densidade)

                    confirmar_para_seguir()
                break
            case 3:
                limpar()
                break
            case _:
                print("\nOpção inválida! Informe uma opção válida de 1 a 2.")
                confirmar_para_seguir()

    return insumos
