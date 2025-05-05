import cv2
from PyQt6.QtGui import QImage, QPixmap
from threads.worker import GSThread
from utils.file_utils import image_dialog

class AppController:
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