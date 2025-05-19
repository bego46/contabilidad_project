from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QFont
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from backend.db_manager import DBManager
from frontend.ui_register import RegistroTransaccion
from frontend.ui_history import HistorialTransacciones
from backend.calculations import calcular_balance



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resumen Financiero")
        self.setGeometry(100, 100, 800, 600)
        self.db = DBManager()

        self.layout = QVBoxLayout()
        self.balance_label = QLabel("Balance Total: $0")
        self.balance_label.setFont(QFont("Arial", 16))

        # Gráfico de ingresos/gastos
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.layout.addWidget(self.balance_label)
        self.layout.addWidget(self.canvas)

        # Botones de navegación
        self.btn_registro = QPushButton("Registrar Transacción")
        self.btn_registro.clicked.connect(self.abrir_registro)

        self.btn_historial = QPushButton("Ver Historial")
        self.btn_historial.clicked.connect(self.abrir_historial)

        self.layout.addWidget(self.btn_registro)
        self.layout.addWidget(self.btn_historial)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # Cargar balance y gráfico
        self.actualizar_balance()

    def actualizar_balance(self):
        """Consulta el balance usando el módulo de cálculos."""
        transacciones = self.db.obtener_transacciones()
        balance = calcular_balance(transacciones)
        self.balance_label.setText(f"Balance Total: ${balance:.2f}")

    def actualizar_grafico(self, ingresos, gastos):
        """Actualiza el gráfico con datos financieros."""
        fig = self.canvas.figure
        fig.clear()
        ax = fig.add_subplot(111)
        ax.bar(["Ingresos", "Gastos"], [ingresos, gastos], color=["green", "red"])
        ax.set_title("Comparación de ingresos y gastos")
        self.canvas.draw()

    def abrir_registro(self):
        """Abre la ventana de registro."""
        self.registro = RegistroTransaccion()
        self.registro.show()

    def abrir_historial(self):
        """Abre la ventana de historial."""
        self.historial = HistorialTransacciones()
        self.historial.show()
