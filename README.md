#  🔐 Generador Seguro de Contraseñas
> Este proyecto consiste en un generador de contraseñas personalizable, creado en Python, que permite al usuario establecer criterios como la longitud y tipos de caracteres (mayúsculas, minúsculas, números, símbolos). El objetivo es generar claves robustas mediante un proceso seguro y confiable, utilizando la biblioteca secrets para garantizar aleatoriedad criptográfica.

#### 📌 Funcionalidades principales
Entrada personalizada por consola.

- Posibilidad de incluir o excluir:

 - Mayúsculas (A-Z)

 - Minúsculas (a-z)

 - Dígitos (0-9)

 - Símbolos especiales (!@#$%...)

- Validación de entradas del usuario.

- Generación de contraseñas seguras de longitud variable.

- Módulo de salida que muestra la contraseña generada.


#### ⚙️ Arquitectura del sistema
> El proyecto está estructurado en tres capas principales según el diagrama de arquitectura:El proyecto está estructurado en tres capas principales según el diagrama de arquitectura:

#### 📄 Formulario de personalización

- Interfaz que recibe parámetros del usuario desde consola.

- Permite definir la longitud y los tipos de caracteres deseados.

####  Lógica de aplicación🧠 Lógica de aplicación

- Valida las entradas del usuario.

- Contiene las reglas de generación de contraseñas.

- Controla el flujo entre entrada y salida.

#### 🧰 Motor generador de contraseñas

- Usa secrets.choice() para seleccionar caracteres de forma segura.

- Aplica los criterios indicados para construir la contraseña final.

#### 🧾 Módulo de salida

- Muestra la contraseña generada.

- Incluye una opción para copiar

> 📌 Referencia visual disponible en el archivo “Diagrama_de_arquitectura.pdf”
