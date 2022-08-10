import sys
import textblob
from PyQt5 import uic
from PyQt5.QtWidgets import *
from googletrans import Translator
from googletrans import LANGUAGES
language = LANGUAGES
translator = Translator()


class UI_translator(QWidget):
    def __init__(self) -> None:
        super(UI_translator, self).__init__()
        uic.loadUi("interface.ui", self)
        self.setWindowTitle("translator")
        self.comboBox.addItems(language.values())
        self.comboBox_2.addItems(language.values())
        self.pushButton.clicked.connect(lambda: self.apply())
        self.comboBox_2.setCurrentText("arabic")
        self.comboBox.setCurrentText("english")

    def apply(self):
        words = textblob.TextBlob(self.textEdit.toPlainText())
        translation = translator.translate(
            words, dest=self.comboBox_2.currentText(), src=self.comboBox.currentText())
        self.textEdit_2.setText(translation.text)


app = QApplication(sys.argv)
window = UI_translator()
window.show()
app.exec_()
