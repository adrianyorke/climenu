import os
import sys
from pathlib import Path

import toml

script_path = str(Path(__file__).resolve().parent)

class Menu:
    """Easily customised menu app written in Python to optimise execution of commonly used CLI commands."""

    def __init__(self) -> None:
        self.clear_screen()
        self.display_menu()

    @staticmethod
    def clear_screen() -> None:
        if sys.platform in ["darwin", "linux"]:
            # Mac or Linux
            os.system("clear")
        else:
            # Windows
            os.system("cls")

    def display_menu(self) -> None:
        with open(f"{script_path}/menu.toml", "r") as f:
            toml_data = toml.load(f)
        pass
        self.menu_options = toml_data["options"]

        print("*" * (100))
        for x in self.menu_options:
            print(f"{x['option']}: {x['description']}")
        print("*" * (100))

    def input_option(self) -> int:
        option = input(f"Please select a menu item: ")
        return option

    def handle_option(self, option: int) -> None:
        cmd = self.menu_options[option]["command"]
        cmd = cmd.replace("{{script_path}}",script_path)
        print(f"{cmd=}")
        os.system(cmd)

    @property
    def number_of_items(self) -> int:
        return len(self.menu_options)


def main(args):
    menu = Menu()
    if len(args) > 1:
        print(f"{args=}")
        option = args[1]
    else:
        option = menu.input_option()
    while True:
        if option.upper() == "Q":
            option = menu.number_of_items
            break
        elif option.isdigit() and 0 < int(option) < menu.number_of_items + 1:
            break
        else:
            print(f"Option must be in range 1-{menu.number_of_items} or 'Q' to Quit")
            # input option again
            option = menu.input_option()
            continue

    option = int(option) - 1
    if menu.menu_options[option]["command"] != "Quit":
        menu.handle_option(option=option)


if __name__ == "__main__":
    main(sys.argv)
