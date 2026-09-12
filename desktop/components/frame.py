from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class Frame(QFrame):
    def __init__(self, parent=None, style=None, layout="vertical"):
        super().__init__(parent)

        self.Style = self.Shape
        self.setObjectName("Frame")

        if isinstance(style, QFrame.Shape):
            self.setFrameShape(style)
        elif style:
            self.setStyleSheet(style)
        else:
            self.setFrameShape(QFrame.Shape.NoFrame)

        if layout == "horizontal":
            self.lay = QHBoxLayout()
        elif layout == "vertical":
            self.lay = QVBoxLayout()
            self.lay.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        self.lay.addStretch()
        self.setLayout(self.lay)

    def addWidget(self, widget):
        self.lay.addWidget(widget)