from flask import Flask
from config import PORT
from controllers.tareas_controller import ping, get_tareas, get_tarea, crear_tarea, actualizar_tarea, eliminar_tarea
from routes.tareas_routes import tareas_bp


app = Flask(__name__)

# Permite recibir/enviar respuestas en formato JSON
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

#funciones de las rutas
app.register_blueprint(tareas_bp, url_prefix='/')



@app.route('/')
def index():
    return 'Servidor con Python y Flask'

if __name__ == '__main__':
    app.run(port=PORT, debug=True)
    print(f"Server is listening on port: {PORT}")

#corre la aplicacion con python app.py