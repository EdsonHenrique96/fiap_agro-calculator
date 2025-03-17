# Entrada de dados (entrada dos dados para realizar os cálculos);
# Saída de dados (como impressões de dados no terminal);
# Atualização de dados numa posição qualquer do vetor;
# Deleção de dados do vetor de dados;
# Ter a opção “sair do programa”;
from utils import delimiter


def menu():

    while True:
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
                while True:
                    print(delimiter)
                    print("Selecione a cultura desejada:\n")
                    print("1. Café")
                    print("2. Soja")
                    print("3. Voltar ao menu principal")
                    print(delimiter)
                    opcao_cultura = int(
                        input("\nDigite o número da cultura desejada: ")
                    )

                    match opcao_cultura:
                        case 1:
                            print("Café :")
                            print("Figura geométrica para cálculo da área: Retângulo")
                            print("Insumos por m²:")
                            print("Calcário dolomítico: 0,3 kg")
                            print("Superfosfato simples: 0,2 kg")
                            print("Fertilizantes: 0,1 kg")
                            print("Agua: 0,5 L")
                        case 2:
                            print("Soja selecionada")
                        case 3:
                            print("Voltar ao menu principal")
                            break
                        case _:
                            print("Opção inválida! Informe uma opção válida de 1 a 2.")
            case 2:
                print("Saída de dados")
            case 3:
                print("Atualização de dados")
            case 4:
                print("Deleção de dados")
            case 5:
                print("Saindo do programa...")
                break
            case _:
                print("Opção inválida! Informe uma opção válida de 1 a 5.")
