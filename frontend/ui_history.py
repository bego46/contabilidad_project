from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QComboBox, QPushButton
from backend.db_manager import DBManager

class HistorialTransacciones(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Historial de Transacciones")
        self.layout = QVBoxLayout()
        self.db = DBManager()

        # Tabla para mostrar transacciones
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(6)
        self.tabla.setHorizontalHeaderLabels(["Fecha", "Mes", "Descripción", "Categoría", "Ingresos", "Gastos"])

        # Filtros
        self.filtro_categoria = QComboBox()
        self.filtro_categoria.addItems(["Todas", "Sueldo", "Gastos", "Educación", "Vivienda"])
        self.filtro_categoria.currentIndexChanged.connect(self.aplicar_filtro)

        self.btn_actualizar = QPushButton("Actualizar")
        self.btn_actualizar.clicked.connect(lambda: self.mostrar_transacciones(self.db.obtener_transacciones()))

        # Agregar elementos a la interfaz
        self.layout.addWidget(self.filtro_categoria)
        self.layout.addWidget(self.btn_actualizar)
        self.layout.addWidget(self.tabla)
        self.setLayout(self.layout)

        # Mostrar datos al iniciar
        self.mostrar_transacciones()

    def mostrar_transacciones(self, transacciones=None):
        """Carga las transacciones desde la base de datos en la tabla."""
        if transacciones is None:
            transacciones = self.db.obtener_transacciones()  # Devuelve objetos Transaccion
        
        self.tabla.setRowCount(len(transacciones))

        for row, transaccion in enumerate(transacciones):
            # Acceder directamente a los atributos en lugar de usar índices
            datos = [
                transaccion.fecha,
                transaccion.mes,
                transaccion.descripcion,
                transaccion.categoria,
                str(transaccion.ingresos),  # Convertir valores numéricos a string
                str(transaccion.gastos)
            ]
            for col, dato in enumerate(datos):
                self.tabla.setItem(row, col, QTableWidgetItem(dato))

    def aplicar_filtro(self):
        """Filtra las transacciones por categoría seleccionada."""
        categoria_seleccionada = self.filtro_categoria.currentText()
        transacciones = self.db.obtener_transacciones()

        if categoria_seleccionada == "Todas":
            transacciones_filtradas = transacciones
        else:
            transacciones_filtradas = [t for t in transacciones if t.categoria == categoria_seleccionada]
        
        self.mostrar_transacciones(transacciones_filtradas)