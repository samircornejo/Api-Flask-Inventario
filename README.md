1. Configurar la Base de Datos (PostgreSQL)
Primero, creamos la base de datos y ejecutamos tu script .sql.

Bash

# 1. Entrar a Postgres y crear la base de datos
sudo -u postgres psql -c "CREATE DATABASE inventario_fravatel;"

# 2. Configurar la contraseña del usuario postgres (la que usaste en Flask)
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'tu_clave_aqui';"

# 3. Montar las tablas y datos iniciales desde tu archivo .sql
sudo -u postgres psql -d inventario_fravatel -f init_db.sql
2. Montar la API (Flask)
Asumiendo que estás dentro de la carpeta Api-Flask-Inventario y que usas uv (que es más rápido para tu i3):

Bash

# 1. Inicializar el entorno y descargar librerías
uv init
uv add flask flask-cors psycopg2-binary

# 2. Crear y activar el entorno virtual
uv venv
source .venv/bin/activate

# 3. Ejecutar la API
uv run python app.py
