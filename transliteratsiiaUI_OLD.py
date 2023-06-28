import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)
        self.setWindowIcon(QIcon("passport.ico"))
        self.setWindowTitle("Транслитерации для загранпаспортов")
        self.start.clicked.connect(self.run)
        self.russian_alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п",
                                 "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ы", "ъ", "э", "ю", "я"]
        self.english_alphabet = ["a", "b", "v", "g", "d", "e", "e", "zh", "z", "i", "i", "k", "l", "m", "n", "o", "p",
                                 "r", "s", "t", "u", "f", "kh", "ts", "ch", "sh", "shch", "", "y", "ie", "e", "iu",
                                 "ia"]

    def run(self):
        finish = ""
        self.finish.clear()
        Fio = self.FIO.toPlainText().lower()
        for char in Fio:
            if char in self.russian_alphabet:
                index = self.russian_alphabet.index(char)
                translit_char = self.english_alphabet[index]
                finish += translit_char
            else:
                finish += char
        self.finish.insertPlainText(finish.upper())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
