# coding: UTF-8
from database.DB import *
from module.Books import *
from module.GUI import *


def main():
    background_image = "no_image"  # Lembrando que esse é o padrão para quando não há BG_image.
    janela_inicial(background_image)  # Outra maneira de esxecutar o padrão, é não passar argumento nessa função
    while True:
        window, event, values = sg.read_all_windows()
        c = DataBaseBiblioteca()  # Objeto de DataBaseBiblioteca para fazer CRUD e Backups
        if event == sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    main()
