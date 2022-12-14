"""
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 31/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
"""


class Polygon:
    def __init__(self, number_sides):
        self.number_sides = number_sides

    # who am I?
    def who_am_i(self):
        if self.number_sides == 3:
            print("I am a triangle")
        elif self.number_sides == 4:
            print("I am a rectangle or square")



    def how_many_sides(self):
        return self.number_sides

    def area(self):
        return "No Area"

    def perimeter(self):
        return "No Perimeter"


class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        # area = (base * height) / 2
        return self.base * self.height / 2


class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        # area= side * side
        return self.side * self.side


class Rectangle(Polygon):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        # area=base*height
        return self.base * self.height


if __name__ == '__main__':
    triangle = Triangle(3, 4)
    square = Square(5)
    rectangle = Rectangle(6, 7)
    print(triangle.area())
    print(square.area())
    print(rectangle.area())
