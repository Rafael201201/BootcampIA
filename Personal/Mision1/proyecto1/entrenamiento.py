#librerias
import re

"""
Expresiones regulares en python
Problemas reales
"""
#codigo
print("Libreria cargada crrectamente")
#ejemplo1
texto="Mi Numero es 12345"
resultado=re.search(r"\d+",texto)
print(f"{texto} Resultado {resultado.group()}")
texto="Mi Numero es 12345-985"
resultado=re.search(r"\d+",texto)
print(f"{texto} Resultado {resultado.group()}")
