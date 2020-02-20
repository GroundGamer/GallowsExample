import os
import time
import random
from dataclasses import dataclass, field
from typing import List


@dataclass
class GallowsAPI:
    _state: bool = True
    errorLetter: int = 0
    letter: List[str] = field(default_factory=list)
    changeListLetter: List[str] = field(default_factory=list)

    def openFile(self):
        word_choice = []
        with open('./Source files/WordsStockRus.txt', 'r', encoding='utf-8') as f:
            for word in f:
                word_choice.append(word.split('\n'))
        random_number_word = random.randint(0, len(word_choice))
        random_word = word_choice.pop(random_number_word-1)[0]
        self.letter += random_word

    def changeWord(self):
        self.openFile()
        changeLetter = []
        for letter in self.letter:
            random_numb = random.randint(0, 1)
            if random_numb == 0:
                changeLetter.append(letter.replace(letter, '_'))
            else:
                changeLetter.append(letter)
        self.changeListLetter += changeLetter

    def playGame(self):
        if self._state:
            self.changeWord()
        print(f'Слово: {str(self.changeListLetter)}')
        print(f'Ошибки({self.errorLetter})')
        print(self.letter)
        self.gameOver()
        selected_letter = input('Ваша буква: ')
        for index, letter in enumerate(self.letter):
            if selected_letter == letter and not selected_letter == self.changeListLetter[index]:
                print(index)
                self.changeListLetter.pop(index)
                self.changeListLetter.insert(index, selected_letter)
                print(letter)
                print(self.changeListLetter[index]+' ### ')
                self._state = False
                self.playGame()
            elif letter == self.changeListLetter[index]:
                pass
            elif selected_letter != letter:
                if letter != self.changeListLetter[index]:
                    if selected_letter == self.changeListLetter[index] and selected_letter != letter:
                        self.cls()
                        self.errorLetter += 1
                        self._state = False
                        self.playGame()

    def gameOver(self):
        menuBack = Menu()
        if self.letter == self.changeListLetter:
            self.cls()
            self._state = True
            self.errorLetter = 0
            self.letter = []
            self.changeListLetter = []
            print('Вы выиграли!')
            time.sleep(3)
            menuBack.mainMenu()

    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')


@dataclass
class Menu:
    def mainMenu(self):
        print('\t"Виселица"')
        print('1 - Начать игру!\n2 - Об игре\n0 - Выход\n')

        selected_number_choice = int(input('Введите ваш выбор: '))

        if selected_number_choice == 1:
            self.startGame()
        elif selected_number_choice == 2:
            self.aboutGame()
        elif selected_number_choice == 0:
            self.cls()
            self.exitGame()
        else:
            print('\nТакой цифры нету!\nВозвращение в главное меню')
            time.sleep(2)
            self.cls()
            self.mainMenu()

    def aboutGame(self):
        self.cls()
        with open('./Source files/About.txt', 'r') as f:
            for text in f:
                print(text)

        print('\n\n9 - Главное меню\n0 - Выход\n')
        selected_number_choice = int(input('Введите ваш выбор: '))

        if selected_number_choice == 9:
            self.cls()
            self.mainMenu()
        elif selected_number_choice == 0:
            self.cls()
            os.system(exit())
        else:
            print('\nТакой цифры нету!\nПопробуйте ещё раз!')
            time.sleep(2)
            self.cls()
            self.aboutGame()

    def exitGame(self):
        self.cls()
        os.system(exit())

    @staticmethod
    def startGame():
        game = GallowsAPI()
        game.playGame()

    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    menu = Menu()
    menu.mainMenu()
