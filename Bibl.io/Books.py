# coding: UTF-8
import os

try:
    from typing import Any
except:
    os.system("pip install typing")
    from typing import Any


class Livros:

    def __init__(self, title: str, vol: int, writer: Any, ed: str, year: int, editor: str, isbn: int, page: int,
                 gender: Any, lang_o: str, lang: str, translate: Any, cover: str) -> None:
        self.title = title
        self.vol = vol
        self.__writer = writer
        a = 0
        t = len(self.__writer)
        if type(self.__writer) == type("string"):
            self.author = writer
        else:
            self.author = ""
            while a < t - 1:
                self.author += self.__writer[a] + ", "
                a += 1
            self.author += "e " + self.__writer[t - 1]
        self.ed = ed
        self.year = year
        self.editor = editor
        self.isbn = isbn
        self.page = page
        self.__gender = gender
        b = 0
        u = len(self.__gender)
        if type(self.__gender) == type("string"):
            self.genders = gender
        else:
            self.genders = ""
            while b < u - 1:
                self.genders += self.__gender[b] + ", "
                b += 1
            self.genders += "e " + self.__gender[u - 1]
        self.lang_o = lang_o
        self.lang = lang
        self.__translate = translate
        c = 0
        v = len(self.__translate)
        if type(self.__translate) == type("string"):
            self.translator = translate
        else:
            self.translator = ""
            while c < v - 1:
                self.translator += self.__translate[c] + ", "
                c += 1
            self.translator += "e " + self.__translate[v - 1]
        self.cover = cover
