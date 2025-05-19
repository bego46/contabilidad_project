import sqlite3
from backend.models import Transaccion

class DBManager:
    def __init__(self, db_name="contabilidad.db"):
        """Inicializa la conexión con la base de datos SQLite."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._crear_tabla()

    def _crear_tabla(self):
        """Crea la tabla si no existe."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transacciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT,
                mes TEXT,
                descripcion TEXT,
                categoria TEXT,
                ingresos REAL,
                gastos REAL
            )
        """)
        self.conn.commit()

    def agregar_transaccion(self, fecha, mes, descripcion, categoria, ingresos, gastos):
        """Inserta una nueva transacción en la base de datos."""
        self.cursor.execute("""
            INSERT INTO transacciones (fecha, mes, descripcion, categoria, ingresos, gastos) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (fecha, mes, descripcion, categoria, ingresos, gastos))
        self.conn.commit()

    def obtener_transacciones(self):
        """Consulta y convierte las transacciones en objetos Python."""
        self.cursor.execute("SELECT * FROM transacciones")
        filas = self.cursor.fetchall()
        return [Transaccion(*fila) for fila in filas]  # Usa la clase modelo


    def cerrar_conexion(self):
        """Cierra la conexión con la base de datos."""
        self.conn.close()
