from utils import delimiter


def get_nome():
    nome = input("Digite o nome da fazenda: ")
    return nome


def get_rua():
    return input("Digite o nome da rua: ")


def get_numero():
    numero = ""

    while True:
        numero = input("Digite o número: ")

        if not numero.isdecimal():
            print("\n***Digite um numero válido (Exemplo: 99)***\n")
        else:
            break

    return int(numero)


def get_bairro():
    return input("Digite o bairro: ")


def get_cidade():
    return input("Digite a cidade: ")


def get_estado():
    return input("Digite o estado: ")


def get_cep():
    cep = ""

    while True:
        cep = input("Digite o CEP: ")

        if len(cep) != 8:
            print("\n***Digitel um CEP válido (8 digitos)***\n")
        elif len(cep) <= 0:
            print("\n***O CEP não pode ser vazio***\n")
        elif not cep.isdecimal():
            print(
                "\n***Valor inválido, deve conter somente números, Exemplo: 99999999***\n"
            )
        else:
            break

    return int(cep)


def get_proprietario():
    return input("Digite o nome do proprietário: ")


def get_telefone():
    telefone = ""

    while True:
        telefone = input("Digite o telefone: ")

        if len(telefone) < 10 or len(telefone) > 11:
            print("\n***Digitel um telefone válido (10 a 11 digitos)***\n")
        elif len(telefone) <= 0:
            print("\n***O Telefone não pode ser vazio***\n")
        elif not telefone.isdecimal():
            print(
                "\n***Valor inválido, deve conter somente números, Exemplo: 11999999999***\n"
            )
        else:
            break

    return int(telefone)


def get_email():
    return input("Digite o email: ")


def form_dados_cadastrais(fazenda: list):
    print("Dados cadastrais:\n")
    fazenda.append(["Nome", get_nome()]),
    fazenda.append(["Rua", get_rua()]),
    fazenda.append(["Numero", get_numero()]),
    fazenda.append(["Bairro", get_bairro()]),
    fazenda.append(["Cidade", get_cidade()]),
    fazenda.append(["Estado", get_estado()]),
    fazenda.append(["CEP", get_cep()]),
    fazenda.append(["Proprietario", get_proprietario()]),
    fazenda.append(["Telefone", get_telefone()]),
    fazenda.append(["Email", get_email()]),
    print(delimiter)
