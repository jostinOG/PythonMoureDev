"""
 * Reto #6
 * INVIRTIENDO CADENAS
 * Fecha publicación enunciado: 07/02/22
 * Fecha publicación resolución: 14/02/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *

"""


def reverse_string(string):
    inverted_string = ""
    str_list = list(string)
    inverted_str_list = list(string)
    for i in range(len(str_list)):
        inverted_str_list[i] = str_list[len(str_list) - 1 - i]
    for i in range(len(inverted_str_list)):
        inverted_string += inverted_str_list[i]
    return inverted_string


def main():
    str = 'Hola mundo'
    print('Original string: ' + str)
    print('inverted string:', reverse_string(str))


if __name__ == '__main__':
    main()
