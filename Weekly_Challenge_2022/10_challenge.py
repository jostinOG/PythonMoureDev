"""
 * Reto #10
 * EXPRESIONES EQUILIBRADAS
 * Fecha publicación enunciado: 07/03/22
 * Fecha publicación resolución: 14/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
"""


# Paso 1: Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
# Paso 2: Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
# Paso 3: Expresión balanceada: { [ a * ( c + d ) ] - 5 }
# Paso 4: Expresión no balanceada: { a * ( c + d ) ] - 5 }
# Paso 5: Crear una función que compruebe si los paréntesis, llaves y corchetes de una expresión están equilibrados.
# Paso 6: Crear una lista con los delimitadores.
# Paso 7: Crear una lista con los delimitadores de apertura.
# Paso 8: Crear una lista con los delimitadores de cierre.
def balanced(expression):
    delimiters = ['(', ')', '{', '}', '[', ']']
    open_delimiters = ['(', '{', '[']
    close_delimiters = [')', '}', ']']
    stack = []
    for char in expression:
        if char in delimiters:
            if char in open_delimiters:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last_open_delimiter = stack.pop()
                if open_delimiters.index(last_open_delimiter) != close_delimiters.index(char):
                    return False
    return len(stack) == 0


# Paso 9: Crear una función que compruebe si los paréntesis, llaves y corchetes de una expresión están equilibrados.
# Paso 10: Comprobar las siguientes expresiones en el programa principal.: { [ a * ( c + d ) ] - 5 } y { a * ( c + d ) ] - 5 }
def main():
    expression = '{ [ a * ( c + d ) ] - 5 }' # True
    print(f'Expression: {expression}')
    print(f'Balanced: {balanced(expression)}')
    expression = '{ a * ( c + d ) ] - 5 }'  # False
    print(f'Expression: {expression}')
    print(f'Balanced: {balanced(expression)}')


if __name__ == '__main__':
    main()
