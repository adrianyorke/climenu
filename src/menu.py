import os
import sys

import toml


class Menu:
    """Easily customised menu app written in Python to optimise execution of commonly used CLI commands."""

    def __init__(self) -> None:
        self.clear_screen()
        self.display_menu()

    @staticmethod
    def clear_screen() -> None:
        os.system("cls")

    def display_menu(self) -> None:
        with open("src/menu.toml", "r") as f:
            toml_data = toml.load(f)
        pass
        self.menu_options = toml_data["options"]

        print("*" * (100))
        for x in self.menu_options:
            print(f"{x['option']}: {x['description']}")
        print("*" * (100))

    def handle_option(self, option: int) -> None:
        cmd = self.menu_options[option]["command"]
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
        while True:
            option = input(f"Please select a menu item: ")
            if option.isdigit() and 0 < int(option) < menu.number_of_items + 1:
                break
            else:
                print(f"Option must be in range: 1-{menu.number_of_items}")
                continue

    option = int(option) - 1
    if menu.menu_options[option]["description"] != "Quit":
        menu.handle_option(option=option)


if __name__ == "__main__":
    main(sys.argv)
