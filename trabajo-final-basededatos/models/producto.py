# Modelo Producto
from bson import ObjectId
from datetime import datetime
from config.database import Database

class Producto:
    def __init__(self):
        self.db = Database().get_database()
        self.collection = self.db.productos
    
    def crear_producto(self, codigo, nombre, categoria, precio, stock_actual, stock_minimo, proveedor_id):
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "categoria": categoria,
            "precio": float(precio),
            "stockActual": int(stock_actual),
            "stockMinimo": int(stock_minimo),
            "proveedorId": ObjectId(proveedor_id),
            "fechaUltimaActualizacion": datetime.now()
        }
        return self.collection.insert_one(producto)
    
    def obtener_por_codigo(self, codigo):
        return self.collection.find_one({"codigo": codigo})
    
    def obtener_todos(self):
        return list(self.collection.find())
    
    def actualizar_stock(self, codigo, nuevo_stock):
        return self.collection.update_one(
            {"codigo": codigo},
            {"$set": {
                "stockActual": nuevo_stock,
                "fechaUltimaActualizacion": datetime.now()
            }}
        )
    
    def productos_stock_bajo(self):
        return list(self.collection.find({
            "$expr": {"$lt": ["$stockActual", "$stockMinimo"]}
        }))
    
    def existe_codigo(self, codigo):
        return self.collection.count_documents({"codigo": codigo}) > 0