import sys
import re

# leer de la entraa estandar (stdin)
for line in sys.stdin:
    # eliminar espacios en blanco y dividir (split)
    words = line.split()
    # TODO 
    # contar proceso
    for word in words:
        # Limpiar la palabra 
        word = re.sub(r"[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑ]+", "", word)

        if not word:
            continue

        print('%s\t%s' % (word, 1))


'''
    Por cada linea que viene del stdin, la guardo en line. 
    Como es un string, con line.split(), por defecto, elimina
    los espacios en blanco de la linea y devuelve una lista con las
    palabras en esa linea.
    Ese listado de palabras los guardo en words. 
    Luego por cada palabra en words, se le asigna el valor 1, correspondiente
    a una aparacion de esa palabra y se lo muestra por el stdout.

    Ej : Para la linea : 
    The Project Gutenberg EBook of Ulysses, by James Joyce

    The 1
    Project 1
    Gutenberg   1 
    EBook   1
    of 1
    Ulysses 1
    by 1
    James 1
    Joyce 1

    Mapper: Lo que hace es dividir el problema grande  en mucho sub problemas pequeños.
'''