# Vista para movimientos
from controllers.movimiento_controller import MovimientoController

class MovimientoView:
    def __init__(self):
        self.controller = MovimientoController()
    
    def mostrar_menu(self):
        while True:
            print("\n" + "-"*30)
            print("   GESTIÓN DE MOVIMIENTOS")
            print("-"*30)
            print("1. Registrar entrada de stock")
            print("2. Registrar salida de stock")
            print("3. Volver")
            
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == "1":
                self.registrar_entrada()
            elif opcion == "2":
                self.registrar_salida()
            elif opcion == "3":
                break
            else:
                print("Opción no válida.")
    
    def registrar_entrada(self):
        print("\n--- Registrar Entrada de Stock ---")
        try:
            codigo = input("Código del producto: ").strip().upper()
            cantidad = int(input("Cantidad a ingresar: "))
            motivo = input("Motivo (ej: Compra a proveedor): ").strip()
            
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
                return
            
            resultado = self.controller.registrar_movimiento(codigo, "entrada", cantidad, motivo)
            print(f"\n{resultado['message']}")
            
        except ValueError:
            print("Error: La cantidad debe ser un número entero")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    def registrar_salida(self):
        print("\n--- Registrar Salida de Stock ---")
        try:
            codigo = input("Código del producto: ").strip().upper()
            cantidad = int(input("Cantidad a retirar: "))
            motivo = input("Motivo (ej: Venta, Devolución): ").strip()
            
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0")
                return
            
            resultado = self.controller.registrar_movimiento(codigo, "salida", cantidad, motivo)
            print(f"\n{resultado['message']}")
            
        except ValueError:
            print("Error: La cantidad debe ser un número entero")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    def mostrar_reporte_movimientos(self):
        print("\n--- Reporte de Movimientos por Período ---")
        try:
            fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ").strip()
            fecha_fin = input("Fecha fin (YYYY-MM-DD): ").strip()
            
            resultado = self.controller.reporte_movimientos(fecha_inicio, fecha_fin)
            
            if resultado['success']:
                movimientos = resultado['movimientos']
                if movimientos:
                    print(f"\n--- Movimientos del {fecha_inicio} al {fecha_fin} ---")
                    print(f"Total de movimientos: {len(movimientos)}")
                    print("-"*60)
                    
                    for mov in movimientos:
                        print(f"{mov['tipo'].upper()} - {mov['fecha'].strftime('%Y-%m-%d %H:%M')}")
                        print(f"   Cantidad: {mov['cantidad']}")
                        print(f"   Motivo: {mov['motivo']}")
                        print(f"   Usuario: {mov['usuario']}")
                        print()
                else:
                    print("No se encontraron movimientos en el período especificado.")
            else:
                print(f"{resultado['message']}")
                
        except Exception as e:
            print(f"Error inesperado: {e}")