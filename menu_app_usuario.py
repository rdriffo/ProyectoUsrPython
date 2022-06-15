# Importación de clases
from Usuario import Usuario
from logger_base import log
from Usuario_dao import UsuarioDAO


opcion = None
while opcion != 5:
    print('Selecciones una Opción ')
    print('1.- Listar Usuarios')
    print('2.- Agregar Usuarios')
    print('3.- Modificar Usuarios')
    print('4.- Eliminar Usuarios')
    print('5.- Salir')
    opcion = int(input('Selecciones una opción : '))
    if opcion == 1:
        usuarioSelecciona = UsuarioDAO.seleccionar()
        for i in usuarioSelecciona:
            log.info(i)
    elif opcion == 2:
        username_var = input('Ingrese el usuarios a registrar : ')
        password_var = input('Ingrese la password a registrar : ')
        insertaUsuario = Usuario(username=username_var, password=password_var)
        restistos_insertado = UsuarioDAO.insertar(insertaUsuario)
        log.info(f'Nuevos registros Insertados {restistos_insertado}')
    elif opcion == 3:
        id_usuario_var = input('Ingrese el Id del Usuario a modificar :')
        username_var = input('Ingrese el nuevo Usuario  : ')
        password_var = input('Ingrese la Nueva Password :')
        actualizarRegistro = Usuario(id_usuario=id_usuario_var, username=username_var, password=password_var)
        registro_actualizado = UsuarioDAO.actualizar(actualizarRegistro)
        log.debug(f'Registro Actualizado {registro_actualizado}')
    elif opcion == 4:
        id_usuario_var = input('Ingrese registro Id del Registro a Eliminar : ')
        eliminarRegistro = Usuario(id_usuario = id_usuario_var)
        registro_eliminado = UsuarioDAO.eliminar(eliminarRegistro)
        log.debug(f'Registro Eliminado : {registro_eliminado}')
    else:
        log.info('Salimos del Programa.....!')


