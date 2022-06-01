# -*- coding: utf-8 -*-
from random import randint as ri


class Board:

    def __init__(self):
        self.board = ['''
        ===+++---> Welcome to Hangman <---+++===
                        +---+
                        |   |
                        |
                        |
                        |
                        |
                        *********
        ''',
                      '''
                        +---+
                        |   |
                        |   0
                        |
                        |
                        |
                        *********
        ''',
                      '''
                        +---+
                        |   |
                        |   0
                        |   |
                        |
                        |
                        *********
        ''',
                      '''
                        +---+
                        |   |
                        |   0
                        |  /|
                        |
                        |
                        *********
        ''',
                      '''
                        +---+
                        |   |
                        |   0
                        |  /|\ 
                        |
                        |
                        *********
        ''',
                      '''
                        +---+
                        |   |
                        |   0
                        |  /|\ 
                        |  /
                        |
                        *********
        ''',
                      '''
                        +---+
                        |   |
                        |   0
                        |  /|\ 
                        |  / \ 
                        |
                        *********
        '''
                      ]


class RandomWordGenerate:

    def __init__(self):
        with open("words.txt", "rt") as file:
            self.in_word = file.readlines()
            self.len_in_word = len(self.in_word)

    def random_word(self):
        return self.in_word[ri(0, self.len_in_word)].strip()


class Hangman(Board, RandomWordGenerate):

    def __init__(self):
        super().__init__()
        init_random = RandomWordGenerate()
        init_random_word = init_random.random_word()
        init_board = Board()
        self.board = init_board.board
        self.word = init_random_word.lower()
        self.__wrongs = []
        self.__guesses = []

    def __right_guess(self, word_in):
        return self.__guesses.append(word_in)

    def __wrong_guess(self, word_in):
        return self.__wrongs.append(word_in)

    def guess_letter(self, letter):
        if letter in self.word and letter not in self.__guesses:
            self.__right_guess(letter)
        elif letter not in self.word and letter not in self.__wrongs:
            self.__wrong_guess(letter)
        else:
            return False
        return True

    def __hide_word(self):
        self.hide = ""
        for letter in self.word:
            if letter not in self.__guesses:
                self.hide += "-"
            else:
                self.hide += letter
        return self.hide

    def hangman_won(self):
        if "-" not in self.__hide_word():
            return True
        return False

    def is_over(self):
        return self.hangman_won() or (len(self.__wrongs) == 6)

    def game_status(self):
        print(self.board[len(self.__wrongs)])
        print(f'Word: {self.__hide_word()}')
        print('\nMissed letters: ', )
        for letter in self.__wrongs:
            print(letter, )
        print()
        print('Correct letters: ', )
        for letter in self.__guesses:
            print(letter, )
        print()


def main():
    hangman = Hangman()
    quit_case = ["quit", "exit", "sair"]

    while not hangman.is_over():
        hangman.game_status()
        user_input = input('Guess a letter: ')
        user_input = user_input.lower()
        if user_input in quit_case:
            print("GG")
            quit()
        else:
            hangman.guess_letter(user_input)

    hangman.game_status()

    if hangman.hangman_won():
        print("YOU GOT IT! YOU ROCKS.")
    else:
        print("GAME OVER! YOU LOSE.")
        print(f"The word was: {hangman.word}")


condition = True
while condition:
    if __name__ == "__main__":
        main()
        yes = ["y", "yes", "s", "sim", "yeah"]
        y_n = input("Run again? ")
        y_n = y_n.lower()
        if y_n not in yes:
            print("GG")
            condition = False
