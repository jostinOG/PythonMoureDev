import random


# Paso 1: Hacer la división entera del número decimal entre 2
# Paso 2: Guardar el módulo de la división entre 2
# Paso 3: Repetir los pasos 1 y 2 hasta obtener 0 en el cociente
# Paso 4: Invertir los módulos guardados
# Paso 5: Concatenar los módulos para obtener el número binario final
# Paso 6 Encapsular el algoritmo en una función de conversión de decimal a binario
def transform_decimal_to_binary(decimal_number):
    binary_number = ''
    while decimal_number != 0:
        binary_number += str(decimal_number % 2)
        decimal_number //= 2
    return binary_number[::-1]


# Paso 7: Crear una función que genere un número decimal aleatorio
def generate_decimal_number():
    return random.randint(1, 100)


# Paso 8: Crear una función que imprima el número decimal y el binario
def print_decimal_and_binary(decimal_number):
    print('Decimal: ' + str(decimal_number))
    print('Binary: ' + transform_decimal_to_binary(decimal_number))


# Paso 9: Crear una función main que genere un número decimal aleatorio y lo imprima en binario
def main():
    decimal_number = generate_decimal_number()
    print_decimal_and_binary(decimal_number)


# Paso 10: Llamar a la función main
if __name__ == '__main__':
    main()
# Paso 11: Ejecutar el programa
# Decimal: 55
# Binary: 110111
# Paso 12: Subir el programa a GitHub
