from dataclasses import dataclass

@dataclass
class Transaccion:
    id: int
    fecha: str
    mes: str
    descripcion: str
    categoria: str
    ingresos: float
    gastos: float
