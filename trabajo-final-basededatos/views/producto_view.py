# Vista para productos
from controllers.producto_controller import ProductoController
from controllers.proveedor_controller import ProveedorController

class ProductoView:
    def __init__(self):
        self.controller = ProductoController()
        self.proveedor_controller = ProveedorController()
    
    def mostrar_menu(self):
        while True:
            print("\n" + "-"*30)
            print("    GESTIÓN DE PRODUCTOS")
            print("-"*30)
            print("1. Agregar producto")
            print("2. Consultar stock")
            print("3. Listar todos los productos")
            print("4. Volver")
            
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "1":
                self.agregar_producto()
            elif opcion == "2":
                self.consultar_stock()
            elif opcion == "3":
                self.listar_productos()
            elif opcion == "4":
                break
    
    def agregar_producto(self):
        print("\n--- Agregar Nuevo Producto ---")
        try:
            # Mostrar proveedores disponibles
            proveedores = self.proveedor_controller.listar_proveedores()['proveedores']
            if not proveedores:
                print("No hay proveedores registrados. Debe crear un proveedor primero.")
                return
            
            print("Proveedores disponibles:")
            for i, prov in enumerate(proveedores, 1):
                print(f"{i}. {prov['nombre']} - {prov['contacto']}")
            
            # Recopilar datos
            codigo = input("Código del producto: ").strip().upper()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            precio = float(input("Precio: "))
            stock_actual = int(input("Stock inicial: "))
            stock_minimo = int(input("Stock mínimo: "))
            
            # Seleccionar proveedor
            idx_proveedor = int(input("Seleccione proveedor (número): ")) - 1
            proveedor_id = str(proveedores[idx_proveedor]['_id'])
            
            datos = {
                'codigo': codigo,
                'nombre': nombre,
                'categoria': categoria,
                'precio': precio,
                'stock_actual': stock_actual,
                'stock_minimo': stock_minimo,
                'proveedor_id': proveedor_id
            }
            
            resultado = self.controller.agregar_producto(datos)
            print(f"\n{resultado['message']}")
            
        except (ValueError, IndexError) as e:
            print(f"Error en los datos ingresados: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    def consultar_stock(self):
        codigo = input("Ingrese el código del producto: ").strip().upper()
        resultado = self.controller.consultar_stock(codigo)
        
        if resultado['success']:
            producto = resultado['producto']
            print(f"\n--- Información del Producto ---")
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Stock actual: {producto['stockActual']}")
            print(f"Stock mínimo: {producto['stockMinimo']}")
            print(f"Precio: ${producto['precio']:.2f}")
            
            if producto['stockActual'] <= producto['stockMinimo']:
                print("ALERTA: Stock por debajo del mínimo!")
        else:
            print(f"{resultado['message']}")
    
    def mostrar_productos_stock_bajo(self):
        resultado = self.controller.productos_stock_bajo()
        productos = resultado['productos']
        
        if productos:
            print(f"\n--- Productos con Stock Bajo ({len(productos)} encontrados) ---")
            for producto in productos:
                print(f"• {producto['codigo']} - {producto['nombre']}")
                print(f"  Stock actual: {producto['stockActual']} | Mínimo: {producto['stockMinimo']}")
                print()
        else:
            print("No hay productos con stock bajo.")
            
    def listar_productos(self):
        print("\n=== LISTA DE PRODUCTOS ===")
        resultado = self.controller.listar_productos()
        if resultado["success"]:
            productos = resultado["productos"]
            if productos:
                for producto in productos:
                    print(f"Código: {producto['codigo']}")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Stock: {producto['stockActual']}")
                    print(f"Precio: ${producto['precio']}")
                    print("-" * 30)
            else:
                print("No hay productos registrados.")
        else:
            print(f"Error: {resultado['message']}")