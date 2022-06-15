# Importación de Clases
from logger_base import log

class Usuario:
    # Método Constructor
    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    def __str__(self):
        return f'''
            Id Usuario  : {self._id_usuario},
            Username    : {self._username},
            Password    : {self._password}
        '''
    
    # Get y Set
    @property
    def id_usuario(self):
        return self._id_usuario
    
    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario= id_usuario

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username= username

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password= password


# Bloque de pruebas Locales
if __name__ == '__main__':
    persona1 = Usuario(1,'rriffo', '123qwe')
    log.debug(persona1)

    #Simular un Insert
    persona2 = Usuario( username='apradena', password='algunaClave')
    log.debug(persona2)

    # Simular Delete
    persona3 = Usuario(id_usuario=1)
    log.debug(persona3)