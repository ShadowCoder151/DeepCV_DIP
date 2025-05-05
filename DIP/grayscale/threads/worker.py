from PyQt6.QtCore import QThread, pyqtSignal
from model.logic import convert_grayscale
import numpy as np

class GSThread(QThread):
    img_used = pyqtSignal(np.ndarray)

    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path

    def run(self):
        gray_img = convert_grayscale(self.image_path)
        self.img_used.emit(gray_img)