# coding: UTF-8
from module.quotes import *
import os

try:
    import PySimpleGUI as sg
except ImportError:
    os.system("pip install PySimpleGUI")
    import PySimpleGUI as sg


def janela_inicial():

    sg.theme("DarkBlue17")

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
        [sg.Image('/home/notebook/Área de Trabalho/Github/Projetos/Python/Bibl.io/img/Bibl-io2.png')]
                ]

    col_frase = [
        [sg.T(""), sg.T(""), sg.T("")],
        [sg.T(""), sg.T(""), sg.T("")],
        [sg.T(""), sg.T(f"{quote_content}"), sg.T("")],
        [sg.T(""),sg.T(""),sg.T(f" - {quote_author}")],
        [sg.T(""), sg.T(""), sg.T("")],
        [sg.T(""), sg.T(""), sg.T("")]
                 ]

    layout = [
        [sg.Menu(menu, background_color='white')],
        [sg.Column(col_logo, pad=(0,(50,50)))],
        [sg.Column(col_frase)]
              ]

    winPrin = sg.Window('Bibl.io', icon=logo, layout=layout, element_justification='center', element_padding=(0, 0),
                            size=(1120, 770), finalize=True)