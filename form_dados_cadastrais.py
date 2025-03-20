from utils import delimiter


def get_nome():
    nome = input("Digite o nome da fazenda: ")
    return nome


def get_rua():
    return input("Digite o nome da rua: ")


def get_numero():
    return input("Digite o número: ")


def get_bairro():
    return input("Digite o bairro: ")


def get_cidade():
    return input("Digite a cidade: ")


def get_estado():
    return input("Digite o estado: ")


def get_cep():
    return input("Digite o CEP: ")


def get_proprietario():
    return input("Digite o nome do proprietário: ")


def get_telefone():
    return input("Digite o telefone: ")


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
