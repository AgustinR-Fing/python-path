from flask import Flask


def create_app(): # Factory
    app = Flask(__name__) # Se crea la instancia

    @app.route("/ping") # Registra la funcion ping() como endpoint de la URL /ping (no modifica la funcion)
    def ping():
        return {"status": "ok"}

    return app