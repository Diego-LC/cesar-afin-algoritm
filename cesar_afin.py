def cifrar(mensaje, k, alfabeto):
    alfabeto = alfabeto.lower()
    mensaje = mensaje.lower()
    resultado = ''
    n = len(alfabeto)
    for char in mensaje:
        if char in alfabeto:
            index = alfabeto.index(char)
            nuevo_index = (index + k) % n # Aritmética modular desplarzar k posiciones
            resultado += alfabeto[nuevo_index]
        else:
            resultado += char
    return resultado

def descifrar(mensaje, k, alfabeto):
    alfabeto = alfabeto.lower()
    mensaje = mensaje.lower()
    resultado = ''
    n = len(alfabeto)
    for char in mensaje:
        if char in alfabeto:
            index = alfabeto.index(char)
            nuevo_index = (index - k) % n
            resultado += alfabeto[nuevo_index]
        else:
            resultado += char
    return resultado

# Pruebas
if __name__ == "__main__":
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mensaje_original = 'un mensaje secreto que se necesita cifrar y descifrar'
    k = 587

    mensaje_cifrado = cifrar(mensaje_original, k, alfabeto)
    mensaje_descifrado = descifrar(mensaje_cifrado, k, alfabeto)

    print(f"Mensaje original: {mensaje_original}")
    print(f"Mensaje cifrado: {mensaje_cifrado}")
    print(f"Mensaje descifrado: {mensaje_descifrado}")

    mensaje_original = 'algoritmo de cesar escrito en python'
    k = 5

    mensaje_cifrado = cifrar(mensaje_original, k, alfabeto)
    mensaje_descifrado = descifrar(mensaje_cifrado, k, alfabeto)

    print(f"\nMensaje original: {mensaje_original}")
    print(f"Mensaje cifrado: {mensaje_cifrado}")
    print(f"Mensaje descifrado: {mensaje_descifrado}")