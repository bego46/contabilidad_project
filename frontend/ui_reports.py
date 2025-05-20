from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog
from backend.db_manager import DBManager
from backend.report_generator import generar_reporte_pdf, exportar_excel

class Reportes(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generar Reportes")
        self.setGeometry(100, 100, 400, 200)
        self.layout = QVBoxLayout()
        self.db = DBManager()

        # Botón para generar PDF
        self.btn_pdf = QPushButton("Generar Reporte en PDF")
        self.btn_pdf.clicked.connect(self.exportar_pdf)

        # Botón para exportar a Excel
        self.btn_excel = QPushButton("Exportar a Excel")
        self.btn_excel.clicked.connect(self.exportar_excel)

        # Agregar botones a la interfaz
        self.layout.addWidget(self.btn_pdf)
        self.layout.addWidget(self.btn_excel)
        self.setLayout(self.layout)

    def exportar_pdf(self):
        """Abre una ventana para elegir donde guardar el PDF."""
        # opciones = QFileDialog.options()
        ruta_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar reporte PDF", "", "PDF Files (*.pdf)")
        if ruta_archivo: # Si el usuario elige una ruta valida
            transacciones = self.db.obtener_transacciones()
            generar_reporte_pdf(transacciones, filename=ruta_archivo)

    def exportar_excel(self):
        """Exporta los datos a Excel."""
        # opciones = QFileDialog.Options()
        ruta_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar reporte Excel", "", "Excel Files (*.xlsx)")
        if ruta_archivo:
            transacciones = self.db.obtener_transacciones()
            exportar_excel(transacciones, filename=ruta_archivo)
