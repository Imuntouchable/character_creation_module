from math import sqrt


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def Calc(your_number: float):
    """Вывод полученного значения."""
    if your_number <= 0:
        return
    print('Мы вычислили квадратный корень '
          'из введённого вами числа. Это '
          'будет: ' + str(CalculateSquareRoot(your_number)))


message: str = ('Добро пожаловать в самую лучшую программу'
                ' для вычисления квадратного корня из заданного числа')

print(message)
Calc(25.5)
