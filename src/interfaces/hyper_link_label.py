"""HyperlinkLabel class"""
from PyQt5.QtWidgets import QLabel


class HyperlinkLabel(QLabel):
    """Create clickable links"""
    def __init__(self, parent=None):
        super().__init__()
        self.setStyleSheet("font-size: 20px")
        self.setOpenExternalLinks(True)
        self.setParent(parent)
