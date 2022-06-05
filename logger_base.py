# Importando clase loggin
import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('LoggerUsuarios.log'),
                    log.StreamHandler()
                ])


# Bloque de pruebas locales
if __name__ == '__main__':
    log.debug('Mensaje a nivel de Debug..')
    log.info('Mensaje a nivel de Info..')
    log.warning('Mensaje a nivel de Warning..')
    log.error('Mensaje a nivel de Error..')
    log.critical('Mensaje a nivel de Critical..')



def loggin():
    return None 
    