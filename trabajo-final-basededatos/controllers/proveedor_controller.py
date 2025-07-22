# Controlador de proveedores
from models.proveedor import Proveedor
from utils.validations import validar_email, validar_telefono

class ProveedorController:
    def __init__(self):
        self.proveedor_model = Proveedor()
    
    def agregar_proveedor(self, datos_proveedor):
        try:
            # Validaciones
            if not validar_email(datos_proveedor['email']):
                return {"success": False, "message": "Email inválido"}
            
            if not validar_telefono(datos_proveedor['telefono']):
                return {"success": False, "message": "Teléfono inválido"}
            
            # Crear proveedor
            resultado = self.proveedor_model.crear_proveedor(**datos_proveedor)
            return {"success": True, "message": "Proveedor agregado exitosamente", "id": str(resultado.inserted_id)}
        except Exception as e:
            return {"success": False, "message": f"Error: {str(e)}"}
    
    def listar_proveedores(self):
        try:
            proveedores = self.proveedor_model.obtener_todos()
            return {"success": True, "proveedores": proveedores}
        except Exception as e:
            return {"success": False, "message": f"Error: {str(e)}"}
    
    def obtener_proveedor(self, proveedor_id):
        try:
            proveedor = self.proveedor_model.obtener_por_id(proveedor_id)
            if proveedor:
                return {"success": True, "proveedor": proveedor}
            return {"success": False, "message": "Proveedor no encontrado"}
        except Exception as e:
            return {"success": False, "message": f"Error: {str(e)}"}
    
    def agregar_producto_a_proveedor(self, proveedor_id, codigo_producto):
        try:
            resultado = self.proveedor_model.agregar_producto_ofrecido(proveedor_id, codigo_producto)
            if resultado.modified_count > 0:
                return {"success": True, "message": "Producto agregado al proveedor"}
            return {"success": False, "message": "No se pudo agregar el producto"}
        except Exception as e:
            return {"success": False, "message": f"Error: {str(e)}"}