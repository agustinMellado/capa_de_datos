import psycopg2
from psycopg2 import pool
import sys
from logger_base import log

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = '1941'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON= 1
    _MAX_CON= 5
    _pool= None
    _conexion= None
    _cursor= None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                                            cls._MIN_CON,
                                            cls._MAX_CON,
                                            host=cls._HOST,
                                            user=cls._USERNAME,
                                            password=cls._PASSWORD,
                                            port=cls._DB_PORT,
                                            database=cls._DATABASE)
                log.debug(f'Creación pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Error al crear el pool de conexiones: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        #Obtener una conexion del pool
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion
    
    @classmethod
    def liberarConexion(cls, conexion):
        #Regresar el objeto conexion al pool
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool: {conexion}')
        log.debug(f'Estado del pool: {cls._pool}')
        
    @classmethod
    def cerrarConexiones(cls):
        #Cerrar el pool y todas sus conexiones
        cls.obtenerPool().closeall()
        log.debug(f'Cerramos todas las conexiones del pool: {cls._pool}')
        
if __name__ == '__main__':
    #Obtener una conexion a partir del pool
    conexion1 = Conexion.obtenerConexion()
    #conexion2 = Conexion.obtenerConexion()
    #Regresamos las conexiones al pool
    Conexion.liberarConexion(conexion1)
    #Conexion.liberarConexion(conexion2)
    #Cerramos el pool
    #Conexion.cerrarConexiones()
    #Si intentamos pedir una conexion de un pool cerrado manda error 
    #conexion3 = Conexion.obtenerConexion()
