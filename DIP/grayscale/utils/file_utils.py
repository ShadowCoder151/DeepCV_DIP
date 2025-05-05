from PyQt6.QtWidgets import QFileDialog

def image_dialog():
    image_path, _ = QFileDialog.getOpenFileName(None, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
    return image_path
