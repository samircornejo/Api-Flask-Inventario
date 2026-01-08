-- 1. Borrar tabla si existe (para reiniciar limpiamente)
DROP TABLE IF EXISTS productos;

-- 2. Crear la tabla de productos
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(50) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INTEGER DEFAULT 0,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Insertar datos iniciales (Seeders)
INSERT INTO productos (codigo, nombre, precio, stock) VALUES
('REP-001', 'Filtro de Aceite HP', 25.50, 15),
('REP-002', 'Pastillas de Freno Cerámicas', 120.00, 8),
('REP-003', 'Bujía de Iridio', 45.00, 20),
('REP-004', 'Amortiguador Delantero', 210.00, 4);

-- 4. Mensaje de confirmación
SELECT 'Base de datos montada correctamente' AS Estado;