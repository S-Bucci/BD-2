# Modelo Proveedor
from bson import ObjectId
from config.database import Database

class Proveedor:
    def __init__(self):
        self.db = Database().get_database()
        self.collection = self.db.proveedores
    
    def crear_proveedor(self, nombre, contacto, telefono, email, productos_ofrecidos=None):
        proveedor = {
            "nombre": nombre,
            "contacto": contacto,
            "telefono": telefono,
            "email": email,
            "productosOfrecidos": productos_ofrecidos or []
        }
        return self.collection.insert_one(proveedor)
    
    def obtener_todos(self):
        return list(self.collection.find())
    
    def obtener_por_id(self, proveedor_id):
        return self.collection.find_one({"_id": ObjectId(proveedor_id)})
    
    def agregar_producto_ofrecido(self, proveedor_id, codigo_producto):
        return self.collection.update_one(
            {"_id": ObjectId(proveedor_id)},
            {"$addToSet": {"productosOfrecidos": codigo_producto}}
        )