# Importación de Clases
from distutils.log import Log
from cursor_del_pool import CursorDelPool
from logger_base import log
from Usuario import Usuario

# Clase Usuario DAO
class UsuarioDAO:

# Definición de las variables de Clase
    _SELECCIONAR = 'SELECT * FROM usuario'
    _INSERTAR = 'INSERT INTO usuario(username, pasword)	VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, pasword=%s WHERE id_usuario=%s'
    _BORRAR = 'DELETE FROM usuario 	WHERE id_usuario=%s'

    # Método de clase Insertar
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2] )
                usuarios.append(usuario)
            return usuarios

    # Método de clase Insertar
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Los valores insertados son : {usuario} ')
            return cursor.rowcount

    # Método Actualizar
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Los valores actualizados son : {usuario} ')
            return cursor.rowcount

    # Métdo eliminar
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario ,)
            cursor.execute(cls._BORRAR, valores)
            log.debug(f'Los registro eliminados son : {usuario}')
            return cursor.rowcount



    # Bloque de comprobación Local

if __name__ == '__main__':
    # Comprobación del método Insertar
    insertaUsuario = Usuario(username='pcanario', password='357951')
    restistos_insertado = UsuarioDAO.insertar(insertaUsuario)
    log.debug(f'Nuevos registros Insertados {restistos_insertado}')

    # Comprobación del método Actualizar
    actualizarRegistro = Usuario(id_usuario=4, username='folivares', password='555555')
    registro_actualizado = UsuarioDAO.actualizar(actualizarRegistro)
    log.debug(f'Registro Actualizado {registro_actualizado}')

    # Comprobación del método eliminar
    eliminarRegistro = Usuario(id_usuario=11)
    registro_eliminado = UsuarioDAO.eliminar(eliminarRegistro)
    log.debug(f'Registro Eliminado : {registro_eliminado}')

    # Comprobación del método Seleccionar
    usuarioSelecciona = UsuarioDAO.seleccionar()
    for i in usuarioSelecciona:
        log.debug(f'Usuarios Seleccionado : {i}')




