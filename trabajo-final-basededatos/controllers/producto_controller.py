# Controlador de productos
from models.producto import Producto
from models.movimiento import Movimiento
from bson import ObjectId

class ProductoController:
    def __init__(self):
        self.producto_model = Producto()
        self.movimiento_model = Movimiento()
    
    def agregar_producto(self, datos_producto):
        try:
            # Validar que el código no exista
            if self.producto_model.existe_codigo(datos_producto['codigo']):
                return {"success": False, "message": "El código del producto ya existe"}
            
            # Crear producto
            resultado = self.producto_model.crear_producto(**datos_producto)
            
            # Registrar movimiento inicial si hay stock
            if datos_producto['stock_actual'] > 0:
                self.movimiento_model.registrar_movimiento(
                    producto_id=resultado.inserted_id,
                    tipo="entrada",
                    cantidad=datos_producto['stock_actual'],
                    motivo="Stock inicial"
                )
            
            return {"success": True, "message": "Producto agregado exitosamente"}
        except Exception as e:
            return {"success": False, "message": f"Error: {str(e)}"}
    
    def consultar_stock(self, codigo):
        producto = self.producto_model.obtener_por_codigo(codigo)
        if producto:
            return {"success": True, "producto": producto}
        return {"success": False, "message": "Producto no encontrado"}
    
    def productos_stock_bajo(self):
        productos = self.producto_model.productos_stock_bajo()
        return {"success": True, "productos": productos}
    
    def listar_productos(self):
        productos = self.producto_model.obtener_todos()
        return {"success": True, "productos": productos}