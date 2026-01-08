from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="inventario_fravatel",
        user="postgres",
        password="1234"
    )

# 1. LEER (GET ALL)
@app.route('/productos', methods=['GET'])
def listar_productos():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM productos ORDER BY id DESC;')
        productos = cur.fetchall()
        return jsonify(productos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn: conn.close()

# 2. CREAR (POST)
@app.route('/productos', methods=['POST'])
def crear_producto():
    datos = request.json
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO productos (codigo, nombre, precio, stock) VALUES (%s, %s, %s, %s) RETURNING *;',
            (datos['codigo'], datos['nombre'], datos['precio'], datos['stock'])
        )
        nuevo_producto = cur.fetchone()
        conn.commit()
        return jsonify({"mensaje": "Producto creado", "data": nuevo_producto}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        if conn: conn.close()

# 3. ACTUALIZAR (PUT)
@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    datos = request.json
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'UPDATE productos SET codigo=%s, nombre=%s, precio=%s, stock=%s WHERE id=%s;',
            (datos['codigo'], datos['nombre'], datos['precio'], datos['stock'], id)
        )
        conn.commit()
        return jsonify({"mensaje": "Producto actualizado"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        if conn: conn.close()

# 4. ELIMINAR (DELETE)
@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM productos WHERE id = %s;', (id,))
        conn.commit()
        return jsonify({"mensaje": "Producto eliminado"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn: conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)