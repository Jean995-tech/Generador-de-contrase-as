#  🔐 Generador Seguro de Contraseñas
> Este proyecto consiste en un generador de contraseñas personalizable, creado en Python, que permite al usuario establecer criterios como la longitud y tipos de caracteres (mayúsculas, minúsculas, números, símbolos). El objetivo es generar claves robustas mediante un proceso seguro y confiable, utilizando la biblioteca secrets para garantizar aleatoriedad criptográfica.

## 📌 Funcionalidades principales
Entrada personalizada por consola.

- Posibilidad de incluir o excluir:

 - Mayúsculas (A-Z)

 - Minúsculas (a-z)

 - Dígitos (0-9)

 - Símbolos especiales (!@#$%...)

- Validación de entradas del usuario.

- Generación de contraseñas seguras de longitud variable.

- Módulo de salida que muestra la contraseña generada.


### ⚙️ Arquitectura del sistema
> El proyecto está estructurado en tres capas principales según el diagrama de arquitectura:El proyecto está estructurado en tres capas principales según el diagrama de arquitectura:

#### 📄 Formulario de personalización

- Interfaz que recibe parámetros del usuario desde consola.

- Permite definir la longitud y los tipos de caracteres deseados.

#### 🧠 Lógica de aplicación🧠 Lógica de aplicación

- Valida las entradas del usuario.

- Contiene las reglas de generación de contraseñas.

- Controla el flujo entre entrada y salida.

#### 🧰 Motor generador de contraseñas

- Usa **secrets.choice()** para seleccionar caracteres de forma segura.

- Aplica los criterios indicados para construir la contraseña final.

#### 🧾 Módulo de salida

- Muestra la contraseña generada.

- Incluye una opción para copiar (en versiones con GUI).

>📌 Referencia visual disponible en el archivo “Diagrama_de_arquitectura.pdf”

## 🧩 Diagrama de caso de uso🧩 Diagrama de caso de uso
Este diagrama representa las acciones que puede realizar el usuario con el sistema:
Actores:

- Usuario

##### Casos de uso:

- Ingresar opciones (mayúsculas, minúsculas, números, símbolos)

- Crear contraseña

- Generar clave segura

- Copiar contraseña (opcional en interfaz gráfica)

>📝 Ver archivo “Diagrama_de_caso_de_uso.pdf” para detalles visuales📝 Ver archivo “Diagrama_de_caso_de_uso.pdf” para detalles visuales

## 🧪 Código fuente explicado
El núcleo del generador se encuentra en el archivo generador_contrasena.py:
##### Importaciones
```python
import string  # Manejo de caracteres estándar
import secrets  # Generación aleatoria segura
```
##### Función principal
```python
def generar_contrasena(longitud, usar_mayus, usar_minus, usar_digitos, usar_simbolos)
```
- Construye un conjunto de caracteres con base en las preferencias del usuario.

- Utiliza** secrets.choice()** para mayor seguridad.

- Devuelve la contraseña final.
##### Entrada por consola
```python
input("Incluir mayúsculas? (s/n): ")
```
- Se muestra la contraseña generada según las reglas establecidas.

> 💡 El uso de **secrets**  en lugar de random se justifica porque está diseñado para operaciones criptográficamente seguras
..

### 🛠 Requisitos
- Python 3.6 o superior

- No requiere paquetes externos (solo string y **secrets**)

### 🚀 Ejecución
```bash
python generador_contrasena.py
```
### ✍ Autor
Jean Pierre Males
Proyecto académico | 18 de mayo de 2025
