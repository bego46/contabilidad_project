from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QComboBox, QPushButton, QDateEdit, QMessageBox
from PyQt6.QtCore import Qt
from backend.db_manager import DBManager  # Importamos el módulo backend
from backend.calculations import calcular_ingresos_gastos, formatear_numero

class RegistroTransaccion(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Registrar Transacción")
        self.layout = QVBoxLayout()
        self.db = DBManager()  # Instancia del gestor de base de datos

        # Campos de entrada
        self.fecha = QDateEdit()
        self.fecha.setDisplayFormat("dd-MM-yyyy")  # Configurar formato correcto
        self.descripcion = QLineEdit()
        self.categoria = QComboBox()
        self.categoria.addItems(["Sueldo", "Gastos", "Educación", "Vivienda"])
        
        self.ingreso = QLineEdit()
        self.ingreso.setPlaceholderText("0.00")
        self.ingreso.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.ingreso.textChanged.connect(self.formatear_ingreso)
        
        self.gasto = QLineEdit()
        self.gasto.setPlaceholderText("0.00")
        self.gasto.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.gasto.textChanged.connect(self.formatear_gasto)

        # Botón para guardar en la base de datos
        self.btn_guardar = QPushButton("Guardar Transacción")
        self.btn_guardar.clicked.connect(self.guardar_transaccion)

        # Agregamos elementos a la GUI
        self.layout.addWidget(self.fecha)
        self.layout.addWidget(self.descripcion)
        self.layout.addWidget(self.categoria)
        self.layout.addWidget(self.ingreso)
        self.layout.addWidget(self.gasto)
        self.layout.addWidget(self.btn_guardar)
        self.setLayout(self.layout)

    def guardar_transaccion(self):
        """Obtiene los datos de los campos y los guarda en la base de datos."""
        fecha = self.fecha.date().toString("dd-MM-yyyy")  # Solución al formato de fecha
        mes = fecha.split("-")[1]  # Extraemos el mes
        descripcion = self.descripcion.text()
        categoria = self.categoria.currentText()
        ingreso = float(self.ingreso.text()) if self.ingreso.text() else 0
        gasto = float(self.gasto.text()) if self.gasto.text() else 0
        
        # Si no hay ingreso ni gasto, mostramos un mensaje de error
        if not descripcion or not categoria or (ingreso == 0 and gasto == 0):
            QMessageBox.warning(self, "Error", "Debe ingresar al menos un valor valido.")
            return

        # Guardamos en la base de datos
        self.db.agregar_transaccion(fecha, mes, descripcion, categoria, ingreso, gasto)
        
        # Actualizamos el grafico
        self.main_window.actualizar_balance()
        
        # Cerrar ventana despues de guardar
        # self.close()
        
    def formatear_ingreso(self):
        """Aplica formato mientras el usuario escribe, sin mover el cursor."""
        texto = self.ingreso.text().replace(",", "")
        if texto and texto.replace(".", "").isdigit():
            cursor_pos = self.ingreso.cursorPosition()  # 🔹 Guardamos la posición actual del cursor
            self.ingreso.setText(formatear_numero(float(texto)))
            self.ingreso.setCursorPosition(cursor_pos)  # 🔹 Restauramos la posición del cursor

    def formatear_gasto(self):
        """Aplica formato mientras el usuario escribe, sin mover el cursor."""
        texto = self.gasto.text().replace(",", "")
        if texto and texto.replace(".", "").isdigit():
            cursor_pos = self.gasto.cursorPosition()
            self.gasto.setText(formatear_numero(float(texto)))
            self.gasto.setCursorPosition(cursor_pos)