from app import create_app

app = create_app() # Invoco la funcion que defini en app/__init__

if __name__ == "__main__":
    app.run(debug=True) # Arranca el servidor de desarrollo