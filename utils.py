import os
import platform

delimiter = "----------------------------------"


def limpar():
    os.system("cls" if platform.system() == "Windows" else "clear")


def formatar_numero(valor: float) -> str:
    if valor.is_integer():
        return f"{valor:.0f}".replace(".", ",")

    return f"{valor:.2f}".replace(".", ",")


def confirmar_para_seguir():
    input("\nPressione Enter para continuar...")
    limpar()
