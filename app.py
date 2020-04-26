import sys
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
)


SCREEN_SIZE = [700, 700]
CITIES = ["Екатеринбург", "Москва", "Санкт-Петербург", "Красноуфимск"]


class MapQuest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # window settings
        self.setFixedSize(*SCREEN_SIZE)
        self.setWindowTitle("Map Quest")

        # main layout
        vertical_layout = QVBoxLayout()

        # main widget
        centralWidget = QWidget(self)
        centralWidget.setLayout(vertical_layout)
        self.setCentralWidget(centralWidget)

        # editing line for answer
        self.answer_input = QLineEdit()
        self.answer_input.setStyleSheet("""
            background-color: yellow;
            color: darkblue;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: beige;
            font: bold 14px;
            min-width: 10em;
            padding: 6px;
        """)
        self.answer_input.setPlaceholderText("Ready to give an answer?)")
        # self.search_input.returnPressed.connect(self.newSearchRequest)

        # button for check answer
        answer_button = QPushButton()
        answer_button.setText("Check")
        answer_button.setStyleSheet("""
            background-color: red;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: beige;
            font: bold 14px;
            min-width: 10em;
            padding: 6px;
        """)
        # search_button.clicked.connect(self.newSearchRequest)

        # layout for answer widgets
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.answer_input)
        horizontal_layout.addWidget(answer_button)

        # map
        self.mapLabel = MapLabel(CITIES)

        # give up button
        give_up_button = QPushButton()
        give_up_button.setText("I'm tired. Give up!")
        give_up_button.setStyleSheet("""
            background-color: #30d5c8;
            color: darkblue;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: beige;
            font: bold 14px;
            min-width: 10em;
            padding: 6px;
        """)
        # reset_search_result_button.clicked.connect(self.resetSearchResult)

        # adding all layouts and widgets to main layout
        vertical_layout.addWidget(self.mapLabel, alignment=Qt.AlignCenter)
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addWidget(give_up_button, alignment=Qt.AlignCenter)

        # show first city
        self.mapLabel.nextSlide()

        # show window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    quest = MapQuest()
    sys.exit(app.exec_())
