# coding: UTF-8
import os

try:
    from typing import Any
except ImportError:
    os.system("pip install typing")
    from typing import Any


class Livros:

    def __init__(self, title: str, vol: int, writer: Any, ed: str, year: int, editor: str, isbn: int, page: int,
                 gender: Any, original_lang: str, lang: str, translate: Any, cover: str) -> None:
        self.title = title
        self.vol = vol
        self.__writer = writer
        count_escritores = 0
        qtd_escritores = len(self.__writer)
        if isinstance(self.__writer, str):
            self.author = writer
        else:
            self.author = ""
            while count_escritores < qtd_escritores - 1:
                self.author += self.__writer[count_escritores] + ", "
                count_escritores += 1
            self.author += "e " + self.__writer[qtd_escritores - 1]
        self.ed = ed
        self.year = year
        self.editor = editor
        self.isbn = isbn
        self.page = page
        self.__gender = gender
        count_generos = 0
        qtd_generos = len(self.__gender)
        if isinstance(self.__gender, str):
            self.genders = gender
        else:
            self.genders = ""
            while count_generos < qtd_generos - 1:
                self.genders += self.__gender[count_escritores] + ", "
                count_escritores += 1
            self.genders += "e " + self.__gender[qtd_generos - 1]
        self.original_lang = original_lang
        self.lang = lang
        self.__translate = translate
        count_tradutores = 0
        qtd_tradutores = len(self.__translate)
        if isinstance(self.__translate, str):
            self.translator = translate
        else:
            self.translator = ""
            while count_tradutores < qtd_tradutores - 1:
                self.translator += self.__translate[count_escritores] + ", "
                count_escritores += 1
            self.translator += "e " + self.__translate[qtd_tradutores - 1]
        self.cover = cover
