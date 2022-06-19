# coding: UTF-8
from database.DB import *
from module.Books import *
from module.GUI import *


def main():
    janela_inicial()
    while True:
        window, event, values = sg.read_all_windows()
        c = DataBaseBiblioteca()  # Objeto de DataBaseBiblioteca para fazer CRUD e Backups
        if event == sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    main()
