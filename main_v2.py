#Importación del framework
from flask import Flask

#Nombre del app
app = Flask(__name__)

@app.route("/")
def index():
    return "HOLA MUNDO FLASK ACTUALIZACION DEL SERVER AY PADRINO"

@app.route("/hola")
def hola():
    return "Hola desde hola"

@app.route("/nueva")
def nueva():
    return "Hola desde nueva"
    
if __name__ == "__main__":
    app.run(debug = True, port=3000)