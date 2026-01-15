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
print(resultado.group())