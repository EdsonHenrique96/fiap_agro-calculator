import os
import platform

delimiter = "----------------------------------"


def limpar():
    os.system("cls" if platform.system() == "Windows" else "clear")


__all__ = ["delimiter"]
