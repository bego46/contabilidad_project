import sys
from PyQt6.QtWidgets import QApplication
from frontend.ui_main import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
