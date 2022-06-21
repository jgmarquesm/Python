# coding: UTF-8
from module.quotes import *

try:
    import PySimpleGUI as sg
except ImportError:
    os.system("pip install PySimpleGUI")
    import PySimpleGUI as sg

sg.Window._move_all_windows = True


def title_bar(title, text_color, background_color):
    bc = background_color
    tc = text_color
    font = 'Helvetica 12'

    return [sg.Col([[sg.T(title, text_color=tc, background_color=bc, font=font, grab=True)]], pad=(0, 0),
                   background_color=bc),
            sg.Col([[sg.T('_', text_color=tc, background_color=bc, enable_events=True, font=font, key='-MINIMIZE-'),
                     sg.Text('❎', text_color=tc, background_color=bc, font=font, enable_events=True, key='Exit')]],
                   element_justification='r', key='-C-', grab=True,
                   pad=(0, 0), background_color=bc)]


def window_template():
    quote = random_quote()
    quote_content, quote_author = quote[0], quote[1]
    logo = r"/home/notebook/Área de Trabalho/Github/Projetos/Python/Bibl.io/img/Bibl-io.ico"

    menu = [
        ['Reservar', ["Inserir reserva", "Atualizar reserva"]],
        ['Consultar', ['Livros', 'Alunos', 'Reservas']],
        ['Atualizar', ['Alterar dados de um livro', 'Alterar cadastro de aluno']],
        ['Cadastrar', ['Cadastrar um novo livro', 'Cadastrar um novo aluno']],
        ['Ajuda', ['Como cadastrar um livro', 'Como atualizar dados de um livro', 'Como cadastrar um aluno',
                   'Como atualizar dados de um aluno', 'Como inserir uma reserva', 'Como atualizar uma reserva']]
    ]

    col_logo = [
        [sg.Image(r'/home/notebook/Área de Trabalho/Github/Projetos/Python/Bibl.io/img/Bibl-io2.png')]
    ]

    col_frase = [
        [sg.Push(), sg.T(f"{quote_content}"), sg.Push()],
        [sg.Push(), sg.T(f" - {quote_author}")]
    ]

    layout = [
        [sg.Menu(menu)],
        [sg.Column(col_logo)],
        [sg.VPush()],
        [sg.Column(col_frase)],
        [sg.VPush()],
        [sg.Text("Powered by João Gabriel", font="ComicSans 10 underline", text_color="#0000FF")]
    ]

    return sg.Window('Bibl.io', icon=logo, layout=layout, element_justification='center', element_padding=(0, 0),
                     size=(1200, 650), finalize=True)


def janela_inicial(background_image="no_image"):

    sg.theme("BlueMono")  # BlueMono, SystemDefaultForReal

    if background_image == "no_image":

        window_template()

    else:
        background_layout = [[sg.Image(data=background_image)]]
        window_background = sg.Window('Background', background_layout, element_padding=(0, 0), margins=(0, 0),
                                      size=(1200, 650), finalize=True)

        window_background.send_to_back()
        window_template()
        window_template().bring_to_front()
