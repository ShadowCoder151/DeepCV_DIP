from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
from controller.app_control import AppController

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Grayscale Converter')
        self.setGeometry(100, 100, 800, 600)

        # UI Elements
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gray_label = QLabel(self)
        self.gray_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.load_button = QPushButton('Load Image', self)
        self.convert_button = QPushButton('Convert to Grayscale', self)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.gray_label)
        layout.addWidget(self.load_button)
        layout.addWidget(self.convert_button)
        self.setLayout(layout)

        # Controller binding
        self.controller = AppController(self)
        self.load_button.clicked.connect(self.controller.load_image)
        self.convert_button.clicked.connect(self.controller.convert_image)
