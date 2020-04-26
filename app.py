import sys
from random import choice
from PyQt5.QtCore import Qt
from ui_models.map_label import MapLabel
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QLineEdit,
    QWidget,
    QVBoxLayout,
    QLabel,
    QMessageBox,
)
from constants import *


SCREEN_SIZE = [600, 600]
CITIES = ["Екатеринбург", "Москва", "Санкт-Петербург", "Красноуфимск"]


class MapQuest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.right_answers = 0
        self.initUI()

    def initUI(self):
        # window settings
        self.setFixedSize(*SCREEN_SIZE)
        self.setWindowTitle("Map Quest")
        self.setStyleSheet(MAIN_WINDOW_STYLE)

        # main layout
        vertical_layout = QVBoxLayout()

        # main widget
        centralWidget = QWidget(self)
        centralWidget.setLayout(vertical_layout)
        self.setCentralWidget(centralWidget)

        # motivation text
        self.motivation_label = QLabel()
        self.motivation_label.setStyleSheet(MOTIVATION_LABEL_STYLE)
        self.newMotivation()

        # map
        self.mapLabel = MapLabel(CITIES)

        # editing line for answer
        self.answer_input = QLineEdit()
        self.answer_input.setStyleSheet(ANSWER_INPUT_EDIT_STYLE)
        self.answer_input.setPlaceholderText("Ready to give an answer?)")
        self.answer_input.returnPressed.connect(self.checkAnswer)

        # button for check answer
        answer_button = QPushButton()
        answer_button.setText("Check")
        answer_button.setStyleSheet(ANSWER_BTN_STYLE)
        answer_button.clicked.connect(self.checkAnswer)

        # layout for answer widgets
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.answer_input)
        horizontal_layout.addWidget(answer_button)

        # give up button
        give_up_button = QPushButton()
        give_up_button.setText("I'm tired. Give up!")
        give_up_button.setStyleSheet(GIVE_UP_BTN_STYLE)
        give_up_button.clicked.connect(self.giveUp)

        # adding all layouts and widgets to main layout
        vertical_layout.addWidget(self.motivation_label, alignment=Qt.AlignCenter)
        vertical_layout.addWidget(self.mapLabel, alignment=Qt.AlignCenter)
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addWidget(give_up_button, alignment=Qt.AlignCenter)

        # show first city
        self.mapLabel.nextSlide()

        # show window
        self.show()

    def checkAnswer(self):
        self.newMotivation()
        if self.mapLabel.checkAnswer(self.answer_input.text()):
            self.right_answers += 1
            self.compliment()
            if not self.mapLabel.nextSlide():
                self.end()
        else:
            self.wrong()
        self.answer_input.clear()

    def giveUp(self):
        self.answer_input.clear()
        if not self.mapLabel.nextSlide():
            self.end()

    def newMotivation(self):
        self.motivation_label.setText(choice(MOTIVATIONS))

    def compliment(self):
        QMessageBox.information(self, "Hurray!", "Answer correct :)")

    def wrong(self):
        QMessageBox.information(self, "Oops", "Wrong answer (:")

    def end(self):
        QMessageBox.information(self, "The end",
                                f"Thank you for participating!\nYou "
                                f"answered correctly {self.right_answers}/{len(CITIES)} questions")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet(MAIN_WINDOW_STYLE)
    quest = MapQuest()
    sys.exit(app.exec_())


# import sys
#
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
#
# class CustomWindow(QMainWindow):
#        def paintEvent(self, event=None):
#            painter = QPainter(self)
#
#            painter.setOpacity(0.7)
#            painter.setBrush(Qt.white)
#            painter.setPen(QPen(Qt.white))
#            painter.drawRect(self.rect())
#
#
# app = QApplication(sys.argv)
#
# # Create the main window
# window = CustomWindow()
#
# window.setWindowFlags(Qt.FramelessWindowHint)
# window.setAttribute(Qt.WA_NoSystemBackground, True)
# window.setAttribute(Qt.WA_TranslucentBackground, True)
#
# # Create the button
# pushButton = QPushButton(window)
# pushButton.setGeometry(QRect(240, 190, 90, 31))
# pushButton.setText("Finished")
# pushButton.clicked.connect(app.quit)
#
# # Center the button
# qr = pushButton.frameGeometry()
# cp = QDesktopWidget().availableGeometry().center()
# qr.moveCenter(cp)
# pushButton.move(qr.topLeft())
#
# # Run the application
# window.showFullScreen()
# sys.exit(app.exec_())
