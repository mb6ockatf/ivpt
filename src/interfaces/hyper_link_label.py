from PyQt5.QtWidgets import QLabel


class HyperlinkLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__()
        self.setStyleSheet("font-size: 20px")
        self.setOpenExternalLinks(True)
        self.setParent(parent)
