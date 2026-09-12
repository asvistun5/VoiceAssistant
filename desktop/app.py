import sys
import os, subprocess
import PyQt6 as qt

from PyQt6.QtWidgets import *

from components.window import MainWindow
from components.layout import MainLayout
from components.frame import Frame


class MainWindow(MainWindow):
    def __init__(self):
        super().__init__()
        
        # set central widget
        self.center = MainLayout(self)

        # Chat
        self.messages = Frame(style="""
            QFrame#Frame {
                background-color: #f9f9f9;
                border: 1px solid #ccc;
                border-radius: 8px;
            }
        """)

        self.title = QLabel("Messages")
        self.title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
        """)

        self.messages.addWidget(self.title)

        # Область сообщений
        self.messages_area = QScrollArea()
        self.messages_area.setWidgetResizable(True)

        messages_container = Frame()

        self.messages_area.setWidget(messages_container)

        self.messages.addWidget(self.messages_area)

        #Commands
        self.commands_frame = Frame(style=Frame.Shape.StyledPanel)
        self.commands_frame.setStyleSheet("""
            background-color: #f0f0f0;
            padding: 4px;
            border: 1px solid #ccc;
            border-radius: 8px;
        """)
        self.commands_frame.lay.setContentsMargins(10, 10, 10, 10)
        self.commands_frame.setFixedWidth(300)

        self.label = QLabel("Commands")
        self.label.setStyleSheet("""
            font-size: 14px;
            border: none;
        """)
        self.commands_frame.addWidget(self.label)

        self.start_btn = QPushButton("Add command")
        self.start_btn.setFixedHeight(40)

        self.commands_frame.addWidget(self.start_btn)

        self.center.add(self.messages)
        self.center.add(self.commands_frame)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        self.messages.setFixedSize(self.center.width() - 325, self.center.height() - 20)