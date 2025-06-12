import string   # Para acceder a letras, dígitos y símbolos
import random   # Para generar selecciones aleatorias
import secrets  # Para generar selecciones más seguras (ideal para contraseñas)

def generar_contrasena(longitud=12, usar_mayus=True, usar_minus=True, usar_digitos=True, usar_simbolos=True):
    """
    Genera una contraseña aleatoria según las opciones dadas:
    - longitud: cantidad de caracteres
    - usar_mayus: incluir mayúsculas A-Z
    - usar_minus: incluir minúsculas a-z
    - usar_digitos: incluir números 0-9
    - usar_simbolos: incluir símbolos como !@#
    """
    caracteres = ""
    if usar_minus:
        caracteres += string.ascii_lowercase  # abcdef...
    if usar_mayus:
        caracteres += string.ascii_uppercase  # ABCDEF...
    if usar_digitos:
        caracteres += string.digits           # 0123456789
    if usar_simbolos:
        caracteres += string.punctuation      # !"#$%...

    if not caracteres:
        return ""

    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contrasena

# Parte principal del programa
if __name__ == "__main__":
    print("=== Generador de Contraseñas ===")
    longitud = int(input("Longitud de la contraseña: "))
    mayus = input("¿Incluir mayúsculas? (s/n): ").strip().lower() == 's'
    minus = input("¿Incluir minúsculas? (s/n): ").strip().lower() == 's'
    digitos = input("¿Incluir números? (s/n): ").strip().lower() == 's'
    simbolos = input("¿Incluir símbolos? (s/n): ").strip().lower() == 's'

    pwd = generar_contrasena(longitud, mayus, minus, digitos, simbolos)
    print("Tu contraseña generada es:", pwd)
