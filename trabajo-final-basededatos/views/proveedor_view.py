# Vista para proveedores
from controllers.proveedor_controller import ProveedorController

class ProveedorView:
    def __init__(self):
        self.controller = ProveedorController()
    
    def mostrar_menu(self):
        while True:
            print("\n" + "-"*30)
            print("   GESTIÓN DE PROVEEDORES")
            print("-"*30)
            print("1. Agregar proveedor")
            print("2. Listar proveedores")
            print("3. Ver detalle de proveedor")
            print("4. Volver")
            
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "1":
                self.agregar_proveedor()
            elif opcion == "2":
                self.listar_proveedores()
            elif opcion == "3":
                self.ver_detalle_proveedor()
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")
    
    def agregar_proveedor(self):
        print("\n--- Agregar Nuevo Proveedor ---")
        try:
            nombre = input("Nombre de la empresa: ").strip()
            contacto = input("Persona de contacto: ").strip()
            telefono = input("Teléfono: ").strip()
            email = input("Email: ").strip()
            
            # Capturar productos ofrecidos
            productos_ofrecidos = []
            print("\nProductos ofrecidos (Enter vacío para terminar):")
            
            contador = 1
            while True:
                producto = input(f"Producto {contador}: ").strip().upper()
                
                if not producto:
                    break
                    
                productos_ofrecidos.append(producto)
                contador += 1
            
            datos = {
                'nombre': nombre,
                'contacto': contacto,
                'telefono': telefono,
                'email': email,
                'productos_ofrecidos': productos_ofrecidos
            }
            
            resultado = self.controller.agregar_proveedor(datos)
            print(f"\n{resultado['message']}")
            
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    def listar_proveedores(self):
        resultado = self.controller.listar_proveedores()
        
        if resultado['success'] and resultado['proveedores']:
            print(f"\n--- Lista de Proveedores ({len(resultado['proveedores'])} encontrados) ---")
            for i, proveedor in enumerate(resultado['proveedores'], 1):
                print(f"{i}. {proveedor['nombre']}")
                print(f"   Contacto: {proveedor['contacto']}")
                print(f"   Teléfono: {proveedor['telefono']}")
                print(f"   Email: {proveedor['email']}")
                
                productos = proveedor.get('productosOfrecidos', [])
                if productos:
                    print(f"   Productos: {', '.join(productos)}")
                else:
                    print(f"   Productos: No se han especificado productos ofrecidos")
                print()
        else:
            print("No hay proveedores registrados.")
    
    def ver_detalle_proveedor(self):
        resultado_lista = self.controller.listar_proveedores()
        
        if not resultado_lista['success'] or not resultado_lista['proveedores']:
            print("No hay proveedores registrados.")
            return
        
        # Mostrar lista para seleccionar
        proveedores = resultado_lista['proveedores']
        print("\n--- Seleccionar Proveedor ---")
        for i, prov in enumerate(proveedores, 1):
            print(f"{i}. {prov['nombre']}")
        
        try:
            idx = int(input("Seleccione proveedor (número): ")) - 1
            proveedor_seleccionado = proveedores[idx]
            
            print(f"\n--- Detalle del Proveedor ---")
            print(f"Nombre: {proveedor_seleccionado['nombre']}")
            print(f"Contacto: {proveedor_seleccionado['contacto']}")
            print(f"Teléfono: {proveedor_seleccionado['telefono']}")
            print(f"Email: {proveedor_seleccionado['email']}")
            
            productos = proveedor_seleccionado.get('productosOfrecidos', [])
            if productos:
                print(f"Productos ofrecidos:")
                for producto in productos:
                    print(f"  • {producto}")
            else:
                print("No tiene productos asignados aún.")
                
        except (ValueError, IndexError):
            print("Selección inválida.")