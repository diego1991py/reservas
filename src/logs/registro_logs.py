import logging
import os

ruta_script = os.path.dirname(__file__)
ruta_archivo = os.path.join(ruta_script, "logs.log")

logger = logging.getLogger(__name__)
logging.basicConfig(filename=ruta_archivo, encoding="utf-8", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

class RegistroLogs:
    def __init__(self):
        self.logger = logger

    def registrar(self, mensaje):
        self.logger.info(mensaje)