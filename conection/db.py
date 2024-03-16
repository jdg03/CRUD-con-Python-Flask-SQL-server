import pyodbc 
from config import DB_SERVER, DB_USER, DB_PASSWORD, DB_DATABASE

# Crea una cadena de conexión
conn_str = f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={DB_SERVER};DATABASE={DB_DATABASE};UID={DB_USER};PWD={DB_PASSWORD}"

# Intenta establecer una conexión
try:
    conn = pyodbc.connect(conn_str)
    print("Conexión exitosa a la base de datos")
except Exception as e:
    print("Error al conectar a la base de datos:", e)

# Asigna la conexión a pool
pool = conn


 

#CODIGO PARA CREAR LA BASE DE DATOS

#Create DATABASE tareas_db

#USE tareas_db;

#CREATE TABLE tareas (
#  id INT PRIMARY KEY IDENTITY,
#  titulo VARCHAR(100) NOT NULL,
#  descripcion VARCHAR(300),
#  estado BIT NOT NULL DEFAULT 0,
#  fecha DATETIME NOT NULL DEFAULT GETDATE()
#);

