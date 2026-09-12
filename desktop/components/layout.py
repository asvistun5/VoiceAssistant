from PyQt6.QtWidgets import *
from .frame import Frame


class MainLayout(Frame):
    def __init__(self, parent=None):
        super().__init__(style="", layout="horizontal")

        parent.setCentralWidget(self)

    def add(self, widget):
        self.layout().addWidget(widget)