#Problema 91
import re

texto = """
juan123@gmail.com
maria.lopez@hotmail.com
"""

usuarios = re.findall(r'([\w\.-]+)@', texto)

print(usuarios)
