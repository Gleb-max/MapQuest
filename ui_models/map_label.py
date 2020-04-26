from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from random import shuffle, choice
from utils.utils import tokenize_word
from map_api.api import coordinates_by_address, get_bytes_map


class MapLabel(QLabel):
    def __init__(self, cities):
        shuffle(cities)
        self.cities = iter(map(tokenize_word, cities))
        self.current_city = None
        self.map_types = ["map", "sat,skl"]
        super().__init__()

    def nextSlide(self):
        try:
            self.current_city = next(self.cities)
            self.updateView()
        except StopIteration:
            return False
        return True

    def updateView(self):
        coordinates = coordinates_by_address(self.current_city)
        if coordinates is None:
            return False
        image = get_bytes_map(coordinates, choice(self.map_types))
        if image is None:
            return False
        pixmap = QPixmap()
        pixmap.loadFromData(image)
        self.setPixmap(pixmap)

    def checkAnswer(self, answer):
        return tokenize_word(answer) == self.current_city

    def getCurrentCity(self):
        return self.current_city
