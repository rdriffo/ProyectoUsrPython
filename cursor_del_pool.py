# Importación de Clases
import logging as log
from Conexion import Conexion

# Creación de la Clase CursorDelPool
class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

   # Definición del método Enter que se utiliza cuando se inicia la llamada a un recurso iniciando el bloque with
    def __enter__(self):
        log.debug(f'Inicio del método with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor


    # Definición del metodo Exit que se llama cuando termiata el bloque with
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_exepcion):
        log.debug(f'Se ejecuta el método __exit__')
        if valor_excepcion:
            self._conexion.rolback()
            log.error(f'Ocurrio una exepción se hace rollback : {valor_excepcion} {tipo_excepcion} {detalle_exepcion}')
        else:
            self._conexion.commit()
            log.debug(f'Se realiza Commit de la transacción :')
            self._cursor.close()
            Conexion.liberarConexion(self._conexion)




# Bloque de prueba local de la clase
if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug(f'Dentro del bloque with')
        cursor.execute('SELECT * FROM persona WHERE id_persona=41')
    #    cursor.execute('INSERT INTO persona(nombre, apellido, email) VALUES ( 'JUAN', 'APABLAZA', 'japablaza@mail.com');')
        log.debug(cursor.fetchall())
