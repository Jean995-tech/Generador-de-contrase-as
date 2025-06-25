import string  # Constantes de letras, dígitos y símbolos
import secrets  # Selecciones aleatorias seguras


def generar_contrasena(
    longitud=12, usar_mayus=True, usar_minus=True, usar_digitos=True, usar_simbolos=True
):
    """
    Genera una contraseña aleatoria según las opciones dadas:
      - longitud: número de caracteres
      - usar_mayus: incluir A-Z
      - usar_minus: incluir a-z
      - usar_digitos: incluir 0-9
      - usar_simbolos: incluir puntuación
    """
    # Construimos el conjunto de caracteres usando comprensión
    caracteres = (
        (string.ascii_lowercase if usar_minus else "")
        + (string.ascii_uppercase if usar_mayus else "")
        + (string.digits if usar_digitos else "")
        + (string.punctuation if usar_simbolos else "")
    )

    if not caracteres:
        # Si no hay caracteres, no podemos generar nada
        raise ValueError("Debes activar al menos un tipo de carácter.")

    # secrets.choice() para seguridad criptográfica
    return "".join(secrets.choice(caracteres) for _ in range(longitud))


if __name__ == "__main__":
    try:
        longitud = int(input("Ingresa la longitud de la contraseña: ").strip())
    except ValueError:
        print("Error: longitud debe ser un número entero.")
        exit(1)

    # Convertimos s/n a booleano
    pregunta = lambda msg: input(msg).strip().lower().startswith("s")
    mayus = pregunta("Incluir mayúsculas? (s/n): ")
    minus = pregunta("Incluir minúsculas? (s/n): ")
    digitos = pregunta("Incluir dígitos?     (s/n): ")
    simbolos = pregunta("Incluir símbolos?    (s/n): ")

    try:
        pwd = generar_contrasena(longitud, mayus, minus, digitos, simbolos)
    except ValueError as e:
        print("Error:", e)
    else:
        print("Contraseña generada:", pwd)
