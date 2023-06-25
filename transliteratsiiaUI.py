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
        self.slovar = {"а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", "ж": "zh", "з": "z", "и": "i",
                  "й": "i",
                  "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
                  "ф": "f",
                  "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch", "ь": "", "ы": "y", "ъ": "ie", "э": "e",
                  "ю": "iu",
                  "я": "ia"}

    def run(self):
        finish = ""
        self.finish.clear()
        Fio = self.FIO.toPlainText().lower()
        for i in range(len(Fio)):
            if Fio[i] in self.slovar:
                finish += self.slovar[Fio[i]]
            else:
                finish += Fio[i]
        self.finish.insertPlainText(finish.upper())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
