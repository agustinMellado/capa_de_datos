import logging as log
#configuracion de loggin para toda la aplicacion

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datafmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_de_datos.log'),
                    log.StreamHandler()
                ]
                )
if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')