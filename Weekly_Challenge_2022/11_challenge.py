# Paso 1: Crear una funcion que reciba dos cadenas como parametro(str1,str2) e imprima otras dos cadenas como salida (out1, out2).
# Paso 2: out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2..
# Paso 3: out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1..
# Paso 4: Crear una funcion principal que probara el programa con los siguientes valores:
# ("brais","moure")
# ("Me gusta Java","Me gusta Kotlin")
# ("Usa el canal de nuestro discord (https://mouredev.com/discord) \"\uD83D\uDD01reto-semanal\" para preguntas, dudas o prestar ayuda a la comunidad","Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.")
# ("Usa el canal de nuestro discord (https://mouredev.com/discord) \"\uD83D\uDD01reto-semanal\" para preguntas, dudas o prestar ayuda a la comunidad","Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.")
# Paso 5: Ejecutar el programa del main().
# Paso 6: Subir el programa a tu repositorio de GitHub.
def get_strings(str1, str2):
    out1 = ""
    out2 = ""
    for i in str1:
        if i not in str2:
            out1 += i
    for i in str2:
        if i not in str1:
            out2 += i

    return out1, out2


def main():
    print(get_strings("brais", "moure"))
    print(get_strings("Me gusta Java", "Me gusta Kotlin"))
    print(get_strings(
        "Usa el canal de nuestro discord (https://mouredev.com/discord) \"\uD83D\uDD01reto-semanal\" para preguntas, dudas o prestar ayuda a la comunidad",
        "Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada."))
    print(get_strings(
        "Usa el canal de nuestro discord (https://mouredev.com/discord) \"\uD83D\uDD01reto-semanal\" para preguntas, dudas o prestar ayuda a la comunidad",
        "Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada."))


if __name__ == '__main__':
    main()
