import sys
from pathlib import Path

from colorama import Fore, Style, init


def show_directory(path, indent=""):
    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(indent + Fore.BLUE + item.name + "/" + Style.RESET_ALL)

            if not item.is_symlink():
                show_directory(item, indent + "    ")
        else:
            print(indent + Fore.GREEN + item.name + Style.RESET_ALL)


def main():
    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Потрібно вказати шлях до папки.")
        return

    path = Path(sys.argv[1])

    try:
        if not path.exists():
            print("Такий шлях не існує.")
            return

        if not path.is_dir():
            print("Вказаний шлях не є папкою.")
            return

        print(Fore.BLUE + path.name + "/" + Style.RESET_ALL)
        show_directory(path, "    ")

    except OSError:
        print("Не вдалося прочитати папку.")

    except RecursionError:
        print("Занадто багато вкладених папок.")


if __name__ == "__main__":
    main()