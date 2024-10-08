# Cifrado César-Afín

## Descripción General

Este proyecto, con base en ciencias de la computación, implementa un cifrado César y cifrado afín consecutivamente utilizando Python y Flask.  
El cifrado César es una técnica de encriptación simple en la se hace uso de la aritmética modular para que cada letra del texto se desplace un número fijo de posiciones en el alfabeto.
El cifrado afín es una generalización del cifrado César, en el que se desplaza un número fijo de posiciones en el alfabeto, pero además se aplica una transformación lineal a cada letra.

Se puede cifrar o descifrar un mensaje utilizando una clave `a` (base) y una `b` (desplazamiento) que indica las transformaciones y posiciones que se desplazarán las letras.

El objetivo principal de este proyecto es proporcionar una interfaz web para cifrar y descifrar mensajes utilizando este método.

## Instalación y ejecución

Para instalar este proyecto, sigue estos pasos:

1. Tener instalado python: <https://www.python.org/downloads/>
2. Clona el repositorio: `git clone https://github.com/Diego-LC/cesar-afin-algoritm.git`
3. Navega al directorio del proyecto: `cd cesar-afin-algoritm`
4. Instala las dependencias: `pip install -r requirements.txt` o bien `pip install flask`

## Uso

Ejecución directa de los algoritmos o desde la interfaz web con flask:

- Ejecución directa:

   ```sh
   python cesar_afin.py
   ```

- Ejecutar con la aplicación Flask:

    ```sh
    python app.py
    ```

  - Abre tu navegador web y navega a `http://127.0.0.1:5000/`.
  - Ingresa el mensaje, selecciona el alfabeto, ingresa la clave y selecciona la acción (cifrar o descifrar).
  - Haz clic en "Procesar" para ver el resultado.

## Capturas de pantalla

![Resultado pruebas](capturas/Captura_2024-08-25_1.png)

### Resultado del cifrado

![Resultado del cifrado](capturas/Captura_2024-08-26_2.png)

### Resultado del descifrado

![Resultado del descifrado](capturas/Captura_2024-08-26_3.png)

### Resultado al cifrar con base no coprima

![Resultado del descifrado](capturas/Captura_2024-08-26_4.png)

### Resultado al descifrar con base no coprima

![Resultado del descifrado](capturas/Captura_2024-08-26_5.png)
