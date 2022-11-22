 
from cursor_del_pool import CursorDelPool
from logger_base import logger
from usuario import Usuario

class UsuarioDAO:
    '''
    DAO (Data Access Object) 
    CRUD: Create-Read-Update-Delete entidad usuario
    '''
    __SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    __INSERTAR = 'INSERT INTO usuario(username,password) VALUES(%s,%s)'
    __ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    __ELIMINAR = 'DELETE FROM usuario WHERE id_usuario = %s'
    
    @classmethod
    def seleccionar(cls):
       with CursorDelPool() as cursor:  
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = usuario(registro[0], registro[1], registro[2], registro[3])
                usuarios.append(usuario)   
            return usuarios   
    
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor: 
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.get_nombre(), usuario.get_apellido())
            cursor.execute(cls.__INSERTAR, valores)
            return cursor.rowcount
            
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor: 
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.username(), usuario.password())
            cursor.execute(cls.__ACTUALIZAR, valores)
            return cursor.rowcount
       
            
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor: 
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario(),)
            cursor.execute(cls.__ELIMINAR, valores)
            return cursor.rowcount              
    
if __name__ == '__main__':
    #Listado de usuarios
   
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        logger.debug(usuarios)