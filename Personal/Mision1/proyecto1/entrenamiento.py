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

texto="Mi Numero es 12345-985"
resultado=re.findall(r"\d+",texto)
print(f"{texto} Resultado {resultado}")

texto="Mi Numero es 123*45-985"
resultado=re.findall(r"\d+",texto)
print(f"{texto} Resultado {resultado}")

documento1="cc.75.055.60"

def clean_id(documento):
    return re.sub(r"\D","",documento)
print(clean_id(documento1))