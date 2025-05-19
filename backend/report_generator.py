from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd

def generar_reporte_pdf(transacciones, filename="reporte.pdf"):
    """Genera un PDF con el resumen de transacciones."""
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "Reporte Financiero")
    
    y = 730
    for t in transacciones:
        c.drawString(100, y, f"{t.fecha} | {t.descripcion} | ${t.ingresos} | ${t.gastos}")
        y -= 20

    c.save()

def exportar_excel(transacciones, filename="reporte.xlsx"):
    """Exporta los datos a un archivo Excel."""
    df = pd.DataFrame([t.__dict__ for t in transacciones])
    df.to_excel(filename, index=False)
