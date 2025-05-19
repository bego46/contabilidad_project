import pandas as pd

def calcular_balance(transacciones):
    """Calcula el balance total basado en ingresos y gastos."""
    ingresos = sum(t.ingresos for t in transacciones)
    gastos = sum(t.gastos for t in transacciones)
    return ingresos - gastos

def calcular_promedio_gastos(transacciones):
    """Devuelve el gasto promedio por categoría."""
    df = pd.DataFrame([t.__dict__ for t in transacciones])
    return df.groupby("categoria")["gastos"].mean().to_dict()
