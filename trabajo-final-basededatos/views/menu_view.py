# Interfaz principal del menú
from views.producto_view import ProductoView
from views.proveedor_view import ProveedorView
from views.movimiento_view import MovimientoView

class MenuView:
    def __init__(self):
        self.producto_view = ProductoView()
        self.proveedor_view = ProveedorView()
        self.movimiento_view = MovimientoView()
    
    def mostrar_menu_principal(self):
        while True:
            print("\n" + "="*50)
            print("       SISTEMA DE GESTIÓN DE INVENTARIO")
            print("="*50)
            print("1. Gestión de Productos")
            print("2. Gestión de Proveedores")
            print("3. Gestión de Movimientos")
            print("4. Reportes")
            print("5. Salir")
            print("-"*50)
            
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "1":
                self.producto_view.mostrar_menu()
            elif opcion == "2":
                self.proveedor_view.mostrar_menu()
            elif opcion == "3":
                self.movimiento_view.mostrar_menu()
            elif opcion == "4":
                self.mostrar_menu_reportes()
            elif opcion == "5":
                print("¡Gracias por usar el sistema!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
    
    def mostrar_menu_reportes(self):
        while True:
            print("\n" + "-"*30)
            print("      MENÚ REPORTES")
            print("-"*30)
            print("1. Productos con stock bajo")
            print("2. Reporte de movimientos por período")
            print("3. Volver al menú principal")
            
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "1":
                self.producto_view.mostrar_productos_stock_bajo()
            elif opcion == "2":
                self.movimiento_view.mostrar_reporte_movimientos()
            elif opcion == "3":
                break
            else:
                print("Opción no válida.")