def cifrar(mensaje, a, b, alfabeto):
    
    if not esCoPrimo(a, len(alfabeto)):
        return "La clave 'a' (base) no es coprima con la longitud del alfabeto"
    
    alfabeto = alfabeto.lower()
    mensaje = mensaje.lower()
    n = len(alfabeto)

    #Cifrado de César
    cifradoCesar = ''
    k = a+b
    for char in mensaje:
        if char in alfabeto:
            index = alfabeto.index(char)
            nuevo_index = (index + k) % n
            cifradoCesar += alfabeto[nuevo_index]
        else:
            cifradoCesar += char

    # Cifrado afín
    cifradoAfin = ''
    for char in cifradoCesar:
        if char in alfabeto:
            index = alfabeto.index(char)
            nuevo_index = (a*index + b) % n
            cifradoAfin += alfabeto[nuevo_index]
        else:
            cifradoAfin += char

    return cifradoAfin

def descifrar(mensaje, a ,b , alfabeto):
    alfabeto = alfabeto.lower()
    mensaje = mensaje.lower()
    n = len(alfabeto)

    if not esCoPrimo(a, len(alfabeto)):
        return "La clave 'a' (base) no es coprima con la longitud del alfabeto"
    
    # Descifrado Afín
    descifradoAfin = ''
    a_inv = inverso_multiplicativo(a, n)
    
    for char in mensaje:
        if char in alfabeto:
            index = alfabeto.index(char)
            nuevo_index = (a_inv*(index - b)) % n
            descifradoAfin += alfabeto[nuevo_index]
        else:
            descifradoAfin += char
    
    # Descifrado de César
    descifradoCesar = ''
    k = a+b
    for char in descifradoAfin:
        if char in alfabeto:
            index = alfabeto.index(char)
            nuevo_index = (index - k) % n
            descifradoCesar += alfabeto[nuevo_index]
        else:
            descifradoCesar += char

    return descifradoCesar

def esCoPrimo(a, n):
    if a == 1:
        return True
    for i in range(2, n):
        if a % i == 0 and n % i == 0:
            return False
    return True

# inverso multiplicativo en aritmética modular (a^-1) es el menor número que (a*a^-1)mod m = 1
def inverso_multiplicativo(a, n):
    for i in range(1, n):
        if (a*i) % n == 1:
            return i
    return None

# Pruebas
if __name__ == "__main__":
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    mensaje_original = 'un mensaje secreto que se necesita cifrar y descifrar'
    a = 587
    b = 123

    mensaje_cifrado = cifrar(mensaje_original, a, b, alfabeto)
    mensaje_descifrado = descifrar(mensaje_cifrado, a, b, alfabeto)

    print(f"Mensaje original: {mensaje_original}")
    print(f"Mensaje cifrado: {mensaje_cifrado}")
    print(f"Mensaje descifrado: {mensaje_descifrado}")

    mensaje_original = 'algoritmo de cesar escrito en python'
    a = 3
    b = 7

    mensaje_cifrado = cifrar(mensaje_original, a, b, alfabeto)
    mensaje_descifrado = descifrar(mensaje_cifrado, a, b, alfabeto)

    print(f"\nMensaje original: {mensaje_original}")
    print(f"Mensaje cifrado: {mensaje_cifrado}")
    print(f"Mensaje descifrado: {mensaje_descifrado}")