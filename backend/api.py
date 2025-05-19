from flask import Flask, jsonify
from backend.db_manager import DBManager

app = Flask(__name__)
db = DBManager()

@app.route("/transacciones", methods=["GET"])
def obtener_transacciones():
    """Devuelve todas las transacciones en formato JSON."""
    transacciones = db.obtener_transacciones()
    return jsonify(transacciones)

if __name__ == "__main__":
    app.run(debug=True)
