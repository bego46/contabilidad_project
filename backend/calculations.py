import pandas as pd

def calcular_ingresos_gastos(transacciones):
    """ Calcular el total de ingresos y gastos. """
    ingresos = sum(t.ingresos for t in transacciones)
    gastos = sum(t.gastos for t in transacciones)
    return ingresos, gastos # Devuelve ambos valores

def calcular_balance(transacciones):
    """Calcula el balance total basado en ingresos y gastos."""
    ingresos = sum(t.ingresos for t in transacciones)
    gastos = sum(t.gastos for t in transacciones)
    return ingresos - gastos

def calcular_promedio_gastos(transacciones):
    """Devuelve el gasto promedio por categoría."""
    df = pd.DataFrame([t.__dict__ for t in transacciones])
    return df.groupby("categoria")["gastos"].mean().to_dict()

def formatear_numero(valor):
    """Convierte un número a formato con separación de miles y dos decimales."""
    if isinstance(valor, (int, float)):  # Asegurar que es un número válido
        return f"{valor:,.2f}"
    return "0.00"  # Si el valor no es válido, devolver un formato neutro