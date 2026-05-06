from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola! Esta es mi aplicación desplegada en Docker para el proyecto DevOps.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)