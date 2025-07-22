# Modelo Movimiento
from bson import ObjectId
from datetime import datetime
from config.database import Database

class Movimiento:
    def __init__(self):
        self.db = Database().get_database()
        self.collection = self.db.movimientos
    
    def registrar_movimiento(self, producto_id, tipo, cantidad, motivo, usuario="admin"):
        movimiento = {
            "productoId": ObjectId(producto_id),
            "tipo": tipo,  # "entrada" o "salida"
            "cantidad": int(cantidad),
            "motivo": motivo,
            "fecha": datetime.now(),
            "usuario": usuario
        }
        return self.collection.insert_one(movimiento)
    
    def obtener_por_periodo(self, fecha_inicio, fecha_fin):
        return list(self.collection.find({
            "fecha": {
                "$gte": fecha_inicio,
                "$lte": fecha_fin
            }
        }).sort("fecha", -1))