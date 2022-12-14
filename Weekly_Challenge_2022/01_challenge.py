"""
 * Reto #1
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 10/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
"""
import unidecode as unidecode


# ¿ES UN ANAGRAMA?
def is_an_anagram(str1, str2):
    is_anagram = False
    if not str1 and str2:
        print("La cadena está vacía")
    else:
        print('\nPrimera Palabra:', str1)
        print('Segunda Palabra:', str2, '\n')
        str1_lower = str1.lower()
        str2_lower = str2.lower()
        str_1 = remove_accents(str1_lower)
        str_2 = remove_accents(str2_lower)
        orderly_str_1 = sort_str(str_1)
        orderly_str_2 = sort_str(str_2)
        print('P1 ORDENADA', orderly_str_1)
        print('P1 ORDENADA', orderly_str_2)
        if set(orderly_str_1) == set(orderly_str_2):
            is_anagram = True
            return is_anagram
    return is_anagram


# Ordenar una cadena
def sort_str(string):
    characters = sorted(string)
    return characters


# Quitar las tildes de una cadena
def remove_accents(str):
    str_sin_tildes = unidecode.unidecode(str)
    return str_sin_tildes


# Main
if __name__ == '__main__':
    string1 = input('Introduce la primera palabra:\n')
    string2 = input('Introduce la segunda palabra:\n')
    result = is_an_anagram(string1, string2)
    print('¿ES UN ANAGRAMA?', result)
