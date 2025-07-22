# Configuración de MongoDB
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class Database:
    _instance = None
    _client = None
    _db = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance
    
    def connect(self, connection_string="mongodb://localhost:27017/", db_name="inventario_db"):
        try:
            self._client = MongoClient(connection_string)
            self._db = self._client[db_name]
            # Test conexión
            self._client.admin.command('ping')
            print("Conexión a MongoDB exitosa")
            return True
        except ConnectionFailure:
            print("Error: No se pudo conectar a MongoDB")
            return False
    
    def get_database(self):
        return self._db
    
    def close_connection(self):
        if self._client:
            self._client.close()