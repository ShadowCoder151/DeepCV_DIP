import numpy as np
import cv2
import sys
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QHBoxLayout


class GSThread(QThread):
    img_used = pyqtSignal(np.ndarray)

    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path

    def convert_grayscale(self, input_img: cv2.Mat):
        h, w, ch = input_img.shape
        out_img = np.zeros((h, w), dtype=np.uint8)

        for y in range(h):
            for x in range(w):
                pixel = input_img[y, x]
                b, g, r = pixel
                val = (0.001 * r + 0.005 * g + 0.995 * b)
                # val = np.average(pixel)
                out_img[y, x] = int(val)
        
        return out_img

    def run(self):
        input_img = cv2.imread(self.image_path)
        gray_img = self.convert_grayscale(input_img)
        self.img_used.emit(gray_img)


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('GrayScale Converter')
        self.setGeometry(100, 100, 800, 600)

        self.image_label = QLabel(self)
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.load_button = QPushButton('Load Image', self)
        self.load_button.clicked.connect(self.load_image)

        self.convert_button = QPushButton('Convert to Grayscale', self)
        self.convert_button.clicked.connect(self.function)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.load_button)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)

        self.image_path = None
        self.original_img = None
        self.grayscale_thread = None

    def load_image(self):
        options = QFileDialog.Option(0)
        self.image_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)", options=options)

        if self.image_path:
            self.og_img = cv2.imread(self.image_path)
            self.show_image(self.og_img)

    def show_image(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img_rgb.shape
        bpl = ch * w
        q_img = QImage(img_rgb.data, w, h, bpl, QImage.Format.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(q_img))

    def function(self):
        if self.image_path:
            self.gthread = GSThread(self.image_path)
            self.gthread.img_used.connect(self.display)
            self.gthread.start()
    
    def display(self, out_img):
        self.show_image(out_img)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())

