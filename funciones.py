# Convertir de cadena de texto a lista
def convertirALista(texto):
    lista = list(texto.split(' '))
    return lista

# Leer un archivo de texto
def leerArchivo(archivo):
    texto = open('ejemplos/{}.txt'.format(archivo), 'r', encoding='utf-8')
    contenido = texto.read()
    texto.close()
    return contenido # Devolvemos el contenido en forma de cadena

# Eliminar los simbolos de puntuación y acentos del texto
def eliminarPuntuacion(texto):
    import string, re, unidecode # Se necesita instalar -> 'pip install Unidecode'
    texto = texto.translate(str.maketrans('', '', string.punctuation)) # Eliminamos puntuación
    texto = unidecode.unidecode(texto) # Eliminamos acentos
    # texto = unidecode.unidecode(texto) # Eliminamos ? y ! que reemplazaron a ¿ y ¡ en la 1ra ejecución
    # Notar que ¿ y ¡ son casos especiales del español y no se eliminan arriba
    # Nota: En donde se elimina la puntuación, lo que se hace es que se cambian: ¿->? y ¡->!,
    # entonces eliminar ¿ y ¡ no tiene sentido. Hay dos posibles soluciones, eliminar ? y !
    # o correr una segunda vez la función de eliminar puntuación.
    # Nota de la nota: La 2da solución no funciona
    texto = re.sub('[?!]', '', texto) # Eliminamos ¿ y ¡
    return texto

def pasarAMinusculas(texto):
    texto = texto.lower()
    return texto

# Elimar saltos de linea y los reemplaza por un ' '
# Nota: esto nos deja dobles espacios y por ende, cadenas vacias en la lista luego de convertir
def eliminarSaltosDeLinea(texto):
    texto = ' '.join(texto.split('\n'))
    return texto

# Eliminar las cadenas vacias que quedan luego de 
def eliminarCadenasVacias(lista):
    while('' in lista):
        lista.remove('')
    return lista

# Evaluar que palabras son aceptadas por el autómata
def evaluar(palabra):
    from dfaProyecto import automata
    d = automata()
    if d.accepts_input(palabra) != True:
        return False
    return True