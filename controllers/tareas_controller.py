from flask import jsonify, request
from conection.db import pool 
from flask import request

def ping():
    try:
        with pool.cursor() as cursor:
            cursor.execute('SELECT 1 + 1 as result')
            result = cursor.fetchone()

            # Extraer los nombres de las columnas
            columns = [column[0] for column in cursor.description]

            # Crear un diccionario a partir de los nombres de las columnas y los valores de la fila
            result_dict = dict(zip(columns, result))

            return jsonify(result_dict)
    except Exception as e:
        print('Error al ejecutar la consulta:', e)
        return jsonify({'error': 'Error en el servidor'}), 500



def get_tareas():
    try:
        with pool.cursor() as cursor:
            cursor.execute('SELECT * FROM tareas')
            tareas = cursor.fetchall()

            # Obtener los nombres de las columnas
            columns = [column[0] for column in cursor.description]

            # Crear una lista de diccionarios para cada fila
            tareas_list = []
            for tarea in tareas:
                tarea_dict = dict(zip(columns, tarea))
                tareas_list.append(tarea_dict)

            return jsonify(tareas_list)
    except Exception as e:
        return jsonify({'message': str(e)}), 500


def get_tarea(id):
    try:
        with pool.cursor() as cursor:
            cursor.execute('SELECT * FROM tareas WHERE id = ?', (id,))
            tarea = cursor.fetchone()
            if tarea:
                # Obtener los nombres de las columnas
                columns = [column[0] for column in cursor.description]
                
                # Crear un diccionario para la tarea
                tarea_dict = dict(zip(columns, tarea))
                
                return jsonify(tarea_dict)
            else:
                return jsonify({'message': 'Tarea no encontrada'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500




def crear_tarea():
    try:
        titulo = request.json['titulo']
        descripcion = request.json['descripcion']
        
        with pool.cursor() as cursor:
            # Ejecutar la inserción de la tarea
            cursor.execute('INSERT INTO tareas(titulo, descripcion) VALUES (?, ?)', (titulo, descripcion))
            pool.commit()
            
            # Obtener el ID de la tarea recién insertada
            cursor.execute('SELECT SCOPE_IDENTITY()')
            tarea_id = cursor.fetchone()[0]
            
            return jsonify({'id': tarea_id, 'titulo': titulo, 'descripcion': descripcion})
    except Exception as e:
        return jsonify({'message': str(e)}), 500

def actualizar_tarea(id):
    try:
        # Extraer datos actualizados del cuerpo JSON de la solicitud
        titulo = request.json.get('titulo')
        descripcion = request.json.get('descripcion')
        
        # Verificar si los datos están presentes
        if not titulo and not descripcion:
            return jsonify({'message': 'Se requiere al menos un campo para actualizar'}), 400
        
        # Construir la consulta SQL para actualizar la tarea
        update_query = 'UPDATE tareas SET '
        parameters = []
        
        if titulo:
            update_query += 'titulo = ?, '
            parameters.append(titulo)
        
        if descripcion:
            update_query += 'descripcion = ?, '
            parameters.append(descripcion)
        
        # Eliminar la coma extra al final de la consulta
        update_query = update_query.rstrip(', ')
        
        # Agregar el ID de la tarea como último parámetro
        parameters.append(id)
        
        # Ejecutar la consulta SQL para actualizar la tarea
        with pool.cursor() as cursor:
            cursor.execute(update_query + ' WHERE id = ?', parameters)
            pool.commit()
            
            # Devolver la respuesta con un mensaje de éxito
            return jsonify({'message': 'Tarea actualizada correctamente'})
    except Exception as e:
        # En caso de error, devolver un mensaje de error con el código de estado HTTP 500
        return jsonify({'message': str(e)}), 500
    
def eliminar_tarea(id):
    try:
        with pool.cursor() as cursor:
            cursor.execute('DELETE FROM tareas WHERE id = ?', (id,))
            pool.commit()
            
            if cursor.rowcount == 0:
                # Si no se encontró ninguna tarea para eliminar, devolvemos un mensaje de error con el código de estado HTTP 404
                return jsonify({'message': 'Tarea no encontrada'}), 404
            else:
                # Si se eliminó correctamente la tarea, devolvemos un mensaje de éxito
                return jsonify({'message': 'Tarea eliminada correctamente'})
    except Exception as e:
        # En caso de error, devolvemos un mensaje de error con el código de estado HTTP 500
        return jsonify({'message': str(e)}), 500

