# Importación de clases externas
from psycopg2 import pool
from logger_base import log
import psycopg2 as db
import sys

# Definición de la clase Conexión
class Conexion:
    # Definicion de las variable privadas de clase
    _DATABASE = 'test_db'
    _USERMANAME = 'postgres'
    _PASSWORD = 'postgres'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = '1'
    _MAX_CON = '6'
    _pool = None

    # Definición de métodos de clase para obtener la conexión
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(  cls._MIN_CON, cls._MAX_CON,
                                                        host=cls._HOST,
                                                        user=cls._USERMANAME,
                                                        password=cls._PASSWORD,
                                                        port=cls._DB_PORT,
                                                        database=cls._DATABASE)
                #log.debug(f'Creación Exitosa de Pool de Conexion...!')
                return cls._pool
            except Exception as e:
                #log.debug(
                 #   f'Ocurrio una exepción al obtener el Pool de Conexión...! {e}')
                sys.exit()
        else:
            return cls._pool


    # Definición del método de clase para obter el Cursor
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        #log.debug(f'Conexión obtenida desde el Pool de Conexión : {conexion}')
        return conexion
    
    # Método para liberar conexiones y devolerlas al Pool
    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        #log.debug(f'Regrasa la conexión al Pool ...! {conexion}')

    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()


    # Pruebas locales de los métodos
if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    conexion6 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion6)
    conexion7 = Conexion.obtenerConexion()
