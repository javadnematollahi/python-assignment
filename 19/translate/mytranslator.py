import sys
# from translate import Translator
from deep_translator import GoogleTranslator
from translator import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow,QApplication

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.LanguageChoices = ['Hindi','English','French','German','Spanish','Persian']
        self.LanguageChoices_translator =['hi','en','fr','de','es','fa']
        self.InputLanguageChoice=self.LanguageChoices_translator[1]
        self.TranslateLanguageChoice=self.LanguageChoices_translator[5]
        self.ui.input.addItems(self.LanguageChoices)
        self.ui.output.addItems(self.LanguageChoices)
        self.ui.input.setCurrentText(self.LanguageChoices[1])
        self.ui.output.setCurrentText(self.LanguageChoices[5])
        self.ui.input.currentIndexChanged.connect(self.indexchange_input)
        self.ui.output.currentIndexChanged.connect(self.indexchange_output)
        self.ui.translate.clicked.connect(self.Translate)


    def Translate(self):
        translator = GoogleTranslator(source=self.InputLanguageChoice, target=self.TranslateLanguageChoice)
        self.ui.target.clear()
        self.Translation = translator.translate(self.ui.source.toPlainText())
        self.ui.target.insertPlainText(self.Translation)

    def indexchange_input(self,index):
        self.InputLanguageChoice=self.LanguageChoices_translator[index]
    def indexchange_output(self,index):
        self.TranslateLanguageChoice=self.LanguageChoices_translator[index]



app=QApplication(sys.argv)

main_translator=Mainwindow()
main_translator.show()


app.exec()






    

