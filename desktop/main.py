import PyQt6 as qt, sys
from PyQt6.QtWidgets import QApplication

from app import MainWindow

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()