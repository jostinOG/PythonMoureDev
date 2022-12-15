"""
/*
 * Reto #7
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 21/02/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */
"""
#Create a program that counts how many times each word is repeated and displays the final count of all of them.
def count_words(text):
    text = text.lower()
    print('\n'+'Original phrase ------->',text,'\n')
    text = remove_punctuation_marks(text)
    print('Sentence without punctuation marks ----->',text,'\n')
    words = text.split()
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
            print(word,'------>',words_count[word],'Veces'+'\n')
        else:
            words_count[word]=1
            print(word,'------>',words_count[word],'Vez'+'\n')

    return words_count

# Remove punctuation marks
def remove_punctuation_marks(text):
    puntuaction_marks = [".", ",", ";", "!", "?", "¿", "¡", "(", ")", "[", "]", "{", "}", "-", "_", "=", "+", "*", "/",
                         "\\", "|", "&", "%", "$", "#", "@", "~", "^", "`", "'", "\""]
    for mark in puntuaction_marks:
        text = text.replace(mark, "")
    return text


def main():
    str=count_words('Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev).')
    print('\nRESULTADO FINAL',str)


if __name__ == '__main__':
    main()
