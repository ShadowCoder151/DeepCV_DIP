import cv2
from PyQt6.QtGui import QImage, QPixmap
from threads.worker import GSThread
from utils.file_utils import image_dialog

class AppController:
    def __init__(self, ui):
        self.ui = ui
        self.image_path = None
        self.og_img = None
        self.gthread = None

    def load_image(self):
        self.image_path = image_dialog()
        if self.image_path:
            self.og_img = cv2.imread(self.image_path)
            self.show_image(self.og_img, self.ui.image_label)

    def show_image(self, img, label):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img_rgb.shape
        bpl = ch * w
        q_img = QImage(img_rgb.data, w, h, bpl, QImage.Format.Format_RGB888)
        label.setPixmap(QPixmap.fromImage(q_img))

    def convert_image(self):
        if self.og_img is not None:
            self.gthread = GSThread(self.og_img)
            self.gthread.img_used.connect(lambda out_img: self.show_image(out_img, self.ui.gray_label))
            self.gthread.start()
