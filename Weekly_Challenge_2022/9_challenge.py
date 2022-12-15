"""
 * Reto #9
 * CÓDIGO MORSE
 * Fecha publicación enunciado: 02/03/22
 * Fecha publicación resolución: 07/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
"""


# Paso 1: Crear un diccionario con las letras y sus correspondientes códigos morse
def dictionary():
    morse_dict = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        ' ': '  ',
        ',': '--..--',
        '.': '.-.-.-',
        '?': '..--..',
        '!': '-.-.--',
        '/': '-..-.',  # Barra diagonal
        '-': '-....-',
        '(': '-.--.',
        ')': '-.--.-',
        '&': '.-...',
        ':': '---...',
        ';': '-.-.-.',
        '=': '-...-',
        '+': '.-.-.',
        '_': '..--.-',
        '"': '.-..-.',
        '$': '...-..-',
        '@': '.--.-.',
        '¿': '..-.-',
        '¡': '--...-'
    }
    return morse_dict


# Paso 2: Crear una función que reciba un string y lo convierta a código morse
def to_morse(text):
    morse_dict = dictionary()
    morse = ''
    for letter in text:
        morse += morse_dict[letter.lower()] + ' '
    return morse


# Paso 3: Crear una función que reciba un código morse y lo convierta a string
def to_text(morse):
    morse_dict = dictionary()
    text = ''
    for letter in morse.split(' '):
        for key, value in morse_dict.items():
            if letter == value:
                text += key
    return text


# Paso 4: Crear una función que detecte si el string es un código morse o un string
def detect(text):
    morse_dict = dictionary()
    if text[0] in morse_dict.values():
        return to_text(text)
    else:
        return to_morse(text)


# Paso 6: Ejecutar la función convert() con un string y un código morse y comprobar que funciona correctamente con ambos casos en una función main()
def main():
    text = 'hola'  # '.... ---
    morse = '.... --- .-.. .-'  # hola
    text_to_morse = detect(text)
    morse_to_text = detect(morse)
    print(text_to_morse)
    print(morse_to_text)


if __name__ == '__main__':
    main()
