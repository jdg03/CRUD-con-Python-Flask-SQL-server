from flask import Blueprint
from controllers.tareas_controller import ping, get_tareas, get_tarea, crear_tarea, actualizar_tarea, eliminar_tarea

# Crear un Blueprint para las rutas de tareas
tareas_bp = Blueprint('tareas', __name__)

# Definir las rutas y asignar las funciones controladoras
tareas_bp.route('/ping')(ping)
tareas_bp.route('/tareas')(get_tareas)
tareas_bp.route('/tareas/<int:id>')(get_tarea)
tareas_bp.route('/tareas', methods=['POST'])(crear_tarea)
tareas_bp.route('/tareas/<int:id>', methods=['PUT'])(actualizar_tarea)
tareas_bp.route('/tareas/<int:id>', methods=['DELETE'])(eliminar_tarea)
