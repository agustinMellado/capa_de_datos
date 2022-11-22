from conexion import Conexion
from logger_base import log

class CursorDelPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None
    
    #inicio de with
    def __enter__(self):
        log.debug('Inicio de with método __enter__') 
        self.__conn = Conexion.obtenerConexion()
        self.__cursor = self.__conn.cursor()
        return self.__cursor
    
    #fin del bloque with
    def __exit__(self, exception_type, exception_value, exception_traceback):
        log.debug('Se ejecuta método __exit__()')
        #if exception_value is not None:
        if exception_value:
            self.__conn.rollback()  
            log.debug(f'Ocurrió una excepción: {exception_value}')  
        else:
            self.__conn.commit() 
            log.debug('Commit de la transacción') 
        #Cerramos el cursor
        self.__cursor.close()    
        #Regresar la conexión al pool
        Conexion.liberarConexion(self.__conn)     
             
if __name__ == '__main__':
    #Obtenemos un cursor  a partir de la conexión del pool
    #with se ejecuta __enter__ y termina con __exit__
    with CursorDelPool() as cursor:  
        cursor.execute('SELECT * FROM usuario')
        log.debug('Listado de usuarios')
        log.debug(cursor.fetchall())    