from PyQt6.QtCore import QProcess
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

from qframelesswindow import FramelessMainWindow


class MainWindow(FramelessMainWindow):
    def __init__(self):
        super().__init__()

        self.assistant_process = None

        self.setWindowTitle("Intelligent Voice Assistant")
        self.setMinimumSize(600, 600)
        self.setGeometry(100, 100, 950, 700)

        frame_geometry = self.frameGeometry()
        screen = QApplication.primaryScreen()
        if screen is not None:
            center_point = screen.availableGeometry().center()
            frame_geometry.moveCenter(center_point)
            self.move(frame_geometry.topLeft())

        menuBar = QMenuBar(self.titleBar)
        menu = QMenu('Assistant', self)
        menu.addAction('Set name', self.set_name)
        menu.addAction('Exit', self.close)
        menuBar.addMenu(menu)
        menuBar.addAction('Start', self.start_assintant)
        menuBar.addAction('Stop', self.stop_assintant)
        menuBar.addAction('Restart', self.restart_assintant)
        self.titleBar.layout().insertWidget(0, menuBar, 0, Qt.AlignmentFlag.AlignLeft)
        self.titleBar.layout().insertStretch(1, 1)
        self.setMenuWidget(self.titleBar)

    def start_assintant(self):
        print("start_assintant")
        if self.assistant_process is not None:
            return

        self.assistant_process = QProcess(self)

        self.assistant_process.readyReadStandardOutput.connect(self.read_output)
        self.assistant_process.readyReadStandardError.connect(self.read_output)
        self.assistant_process.finished.connect(self.assistant_fineshed)

        python = sys.executable
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        manage_py = os.path.join(base_dir, "assistant", "manage.py")

        self.assistant_process.start(python, [manage_py, "run_assistant"])
        print(manage_py)

        
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

    def restart_assintant(self):
        print("restart_assintant")

    def stop_assintant(self):
        print("stop_assintant")
        if self.assistant_process is None:
            return
        
        self.assistant_process.terminate()

        if not self.assistant_process.waitForFinished(3000):
            self.assistant_process.kill()
        
    def read_output(self):
        self.assistant_process.readAllStandardOutput()

    def read_error(self):
        self.assistant_process.readAllStandardError()

    def assistant_fineshed(self):
        print("assistant_fineshed")

        self.assistant_process.deleteLater()
        self.assistant_process = None

        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

    def set_name(self):
        name, ok = QInputDialog.getText(self, "Set Name", "Enter name:")
        if ok and name:
            print(f"Name set to: {name}")

    def closeEvent(self, event):
        if self.assistant_process is not None:
            self.assistant_process.terminate()
            if not self.assistant_process.waitForFinished(3000):
                self.assistant_process.kill()
        event.accept()


QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)