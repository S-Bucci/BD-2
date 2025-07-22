# Controlador de movimientos
from models.movimiento import Movimiento
from models.producto import Producto
from datetime import datetime

class MovimientoController:
    def __init__(self):
        self.movimiento_model = Movimiento()
        self.producto_model = Producto()
    
    def registrar_movimiento(self, codigo_producto, tipo, cantidad, motivo):
        try:
            # Buscar producto
            producto = self.producto_model.obtener_por_codigo(codigo_producto)
            if not producto:
                return {"success": False, "message": "Producto no encontrado"}
            
            # Calcular nuevo stock
            if tipo == "entrada":
                nuevo_stock = producto['stockActual'] + cantidad
            else:  # salida
                if producto['stockActual'] < cantidad:
                    return {"success": False, "message": "Stock insuficiente"}
                nuevo_stock = producto['stockActual'] - cantidad
            
            # Registrar movimiento
            self.movimiento_model.registrar_movimiento(
                producto_id=producto['_id'],
                tipo=tipo,
                cantidad=cantidad,
                motivo=motivo
            )
            
            # Actualizar stock del producto
            self.producto_model.actualizar_stock(codigo_producto, nuevo_stock)
            
            return {"success": True, "message": f"Movimiento registrado. Nuevo stock: {nuevo_stock}"}
        except Exception as e:
            return {"success": False, "message": f"Error: {str(e)}"}
    
    def reporte_movimientos(self, fecha_inicio_str, fecha_fin_str):
        try:
            fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
            fecha_fin = datetime.strptime(fecha_fin_str + " 23:59:59", "%Y-%m-%d %H:%M:%S")
            
            movimientos = self.movimiento_model.obtener_por_periodo(fecha_inicio, fecha_fin)
            return {"success": True, "movimientos": movimientos}
        except Exception as e:
            return {"success": False, "message": f"Error: {str(e)}"}