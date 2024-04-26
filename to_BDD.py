import sqlite3
import pandas as pd

# Paso 1. Cargar datos
path = r'C:/Users/dtorresl/OneDrive - continental.edu.pe/Gerencia Comercial/01 Estudiantes/01 Actualizado/'
df = pd.read_excel(path + 'db.xlsx')

# Paso 2. Limpieza
df.columns = df.columns.str.strip()

# Paso 3. Crear/conectar a SQLite database
connection = sqlite3.connect('PerfilDemo.db')

# Paso 4. Cargar data a SQLite
df.to_sql('Matriculados', connection, if_exists='replace')

# Paso 5. Cerrar connection
connection.close()