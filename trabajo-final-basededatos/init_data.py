from datetime import datetime
from bson import ObjectId
import pymongo

# Configuración de conexión a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["inventario_db"]  # Cambia por el nombre de tu base de datos

def init_database():
    # Limpiar colecciones existentes (opcional)
    db.productos.delete_many({})
    db.proveedores.delete_many({})
    db.movimientos.delete_many({})
    
    # Insertar proveedores
    proveedores = [
        {
            "_id": ObjectId(),
            "nombre": "TechSupply Solutions",
            "contacto": "María González",
            "telefono": "+54-11-4567-8900",
            "email": "ventas@techsupply.com.ar",
            "productosOfrecidos": ["mouse", "teclado", "monitor"]
        },
        {
            "_id": ObjectId(),
            "nombre": "CompuWorld Argentina",
            "contacto": "Carlos Rodríguez",
            "telefono": "+54-11-5432-1098",
            "email": "compras@compuworld.com.ar",
            "productosOfrecidos": ["impresora", "disco duro", "memoria RAM"]
        },
        {
            "_id": ObjectId(),
            "nombre": "Digital Components SA",
            "contacto": "Ana Martínez",
            "telefono": "+54-11-6789-0123",
            "email": "info@digitalcomp.com.ar",
            "productosOfrecidos": ["procesador", "placa madre", "fuente de poder"]
        }
    ]
    
    result_proveedores = db.proveedores.insert_many(proveedores)
    proveedor_ids = result_proveedores.inserted_ids
    
    print(f"Insertados {len(proveedores)} proveedores")
    
    # Insertar productos
    productos = [
        {
            "_id": ObjectId(),
            "codigo": "MOUSE001",
            "nombre": "Mouse Óptico Logitech",
            "categoria": "Periféricos",
            "precio": 2500.00,
            "stockActual": 25,
            "stockMinimo": 5,
            "proveedorId": proveedor_ids[0],
            "fechaUltimaActualizacion": datetime.now()
        },
        {
            "_id": ObjectId(),
            "codigo": "TECL001",
            "nombre": "Teclado Mecánico RGB",
            "categoria": "Periféricos",
            "precio": 8900.00,
            "stockActual": 15,
            "stockMinimo": 3,
            "proveedorId": proveedor_ids[0],
            "fechaUltimaActualizacion": datetime.now()
        },
        {
            "_id": ObjectId(),
            "codigo": "MON001",
            "nombre": "Monitor LED 24 pulgadas",
            "categoria": "Monitores",
            "precio": 45000.00,
            "stockActual": 8,
            "stockMinimo": 2,
            "proveedorId": proveedor_ids[0],
            "fechaUltimaActualizacion": datetime.now()
        },
        {
            "_id": ObjectId(),
            "codigo": "IMP001",
            "nombre": "Impresora Multifunción HP",
            "categoria": "Impresoras",
            "precio": 65000.00,
            "stockActual": 12,
            "stockMinimo": 2,
            "proveedorId": proveedor_ids[1],
            "fechaUltimaActualizacion": datetime.now()
        },
        {
            "_id": ObjectId(),
            "codigo": "HDD001",
            "nombre": "Disco Duro 1TB Western Digital",
            "categoria": "Almacenamiento",
            "precio": 12000.00,
            "stockActual": 30,
            "stockMinimo": 8,
            "proveedorId": proveedor_ids[1],
            "fechaUltimaActualizacion": datetime.now()
        },
        {
            "_id": ObjectId(),
            "codigo": "RAM001",
            "nombre": "Memoria RAM DDR4 8GB",
            "categoria": "Memoria",
            "precio": 18000.00,
            "stockActual": 20,
            "stockMinimo": 6,
            "proveedorId": proveedor_ids[1],
            "fechaUltimaActualizacion": datetime.now()
        },
        {
            "_id": ObjectId(),
            "codigo": "CPU001",
            "nombre": "Procesador Intel Core i5",
            "categoria": "Procesadores",
            "precio": 85000.00,
            "stockActual": 10,
            "stockMinimo": 3,
            "proveedorId": proveedor_ids[2],
            "fechaUltimaActualizacion": datetime.now()
        },
        {
            "_id": ObjectId(),
            "codigo": "MB001",
            "nombre": "Placa Madre ASUS B450",
            "categoria": "Componentes",
            "precio": 35000.00,
            "stockActual": 15,
            "stockMinimo": 4,
            "proveedorId": proveedor_ids[2],
            "fechaUltimaActualizacion": datetime.now()
        },
        {
            "_id": ObjectId(),
            "codigo": "PSU001",
            "nombre": "Fuente de Poder 650W",
            "categoria": "Componentes",
            "precio": 22000.00,
            "stockActual": 18,
            "stockMinimo": 5,
            "proveedorId": proveedor_ids[2],
            "fechaUltimaActualizacion": datetime.now()
        }
    ]
    
    result_productos = db.productos.insert_many(productos)
    producto_ids = result_productos.inserted_ids
    
    print(f"Insertados {len(productos)} productos")
    
    # Insertar movimientos
    movimientos = [
        {
            "_id": ObjectId(),
            "productoId": producto_ids[0],
            "tipo": "entrada",
            "cantidad": 25,
            "motivo": "Compra inicial a proveedor",
            "fecha": datetime.now(),
            "usuario": "admin"
        },
        {
            "_id": ObjectId(),
            "productoId": producto_ids[1],
            "tipo": "entrada",
            "cantidad": 15,
            "motivo": "Compra inicial a proveedor",
            "fecha": datetime.now(),
            "usuario": "admin"
        },
        {
            "_id": ObjectId(),
            "productoId": producto_ids[2],
            "tipo": "entrada",
            "cantidad": 10,
            "motivo": "Compra inicial a proveedor",
            "fecha": datetime.now(),
            "usuario": "admin"
        },
        {
            "_id": ObjectId(),
            "productoId": producto_ids[2],
            "tipo": "salida",
            "cantidad": 2,
            "motivo": "Venta a cliente",
            "fecha": datetime.now(),
            "usuario": "vendedor1"
        },
        {
            "_id": ObjectId(),
            "productoId": producto_ids[4],
            "tipo": "entrada",
            "cantidad": 30,
            "motivo": "Compra inicial a proveedor",
            "fecha": datetime.now(),
            "usuario": "admin"
        },
        {
            "_id": ObjectId(),
            "productoId": producto_ids[6],
            "tipo": "entrada",
            "cantidad": 12,
            "motivo": "Compra inicial a proveedor",
            "fecha": datetime.now(),
            "usuario": "admin"
        },
        {
            "_id": ObjectId(),
            "productoId": producto_ids[6],
            "tipo": "salida",
            "cantidad": 2,
            "motivo": "Venta a cliente",
            "fecha": datetime.now(),
            "usuario": "vendedor2"
        }
    ]
    
    db.movimientos.insert_many(movimientos)
    print(f"Insertados {len(movimientos)} movimientos")
    
    print("Base de datos inicializada correctamente")

if __name__ == "__main__":
    init_database()