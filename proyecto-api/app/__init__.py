import os
from flask import Flask
from dotenv import load_dotenv
from app.database import db

def create_app(): # Factory

    app = Flask(__name__) # Se crea la instancia

    # Configurar el traductor de SQLAlchemy, que instanciamos en database.py
    load_dotenv()
    database_url = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    db.init_app(app) # Le indico al traductor donde tiene que trabajar (cual base de datos)

    # Registrar rutas
    @app.route("/ping") # Registra la funcion ping() como endpoint de la URL /ping (no modifica la funcion)
    def ping():
        return {"status": "ok"}

    return app