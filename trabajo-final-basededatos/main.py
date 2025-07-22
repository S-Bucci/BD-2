from config.database import Database
from views.menu_view import MenuView

def main():
    # Inicializar base de datos
    db = Database()
    if not db.connect():
        print("No se pudo conectar a la base de datos. Verifique que MongoDB esté ejecutándose.")
        return
    
    try:
        # Iniciar aplicación
        menu = MenuView()
        menu.mostrar_menu_principal()
    finally:
        # Cerrar conexión
        db.close_connection()

if __name__ == "__main__":
    main()