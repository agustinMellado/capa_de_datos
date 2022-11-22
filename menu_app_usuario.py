from usuarioDAO import UsuarioDAO
from usuario import Usuario
from logger_base import log

def mostrar_menu():
    while True:
        print('''
        //////////Menu de opciones///////////
            1) Mostrar lista de usuarios.
            2) Agregar Usuario.
            3) Actualizar Usuario
            4) Eliminar Usuario
            5) Salir.
        ////////////////////////////////////
        ''')
        respuesta= int(input('Ingrese una opcion: '))
        if(respuesta== 1):
            lista_usuarios= UsuarioDAO.seleccionar()
            for usuario in lista_usuarios:
                print(usuario)
            mostrar_menu()
        
        elif(respuesta ==2):
            username=input('Ingrese el nombre del usuario: ')
            password= input('Ingrese su contraseña: ')
            
            user=Usuario(username=username, password=password)
            user_agregado= UsuarioDAO.insertar(user)
            log.debug(f'Se agrego con exito el usuario: {user_agregado}')
        elif(respuesta==3):
            iduser=int(input('Ingrese id: '))
            username=input('Ingrese el nombre del usuario: ')
            password= input('Ingrese su contraseña: ')
            user=Usuario(id_usuario=iduser,username=username, password=password)
            user_actualizado= UsuarioDAO.actualizar(user)
            log.debug(f'Se actualizo con exito el usuario: {user_actualizado}')
        elif(respuesta==4):
            iduser=int(input('Ingrese ID del usuario a eliminar: '))
            user= Usuario(id_usuario=iduser)
            user_eliminado= UsuarioDAO.eliminar(user)
            log.debug(f'Usuario eliminado con exito')
        elif(respuesta==5):
            print('salida')
            break



mostrar_menu()