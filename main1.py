
import logging

logging.basicConfig(level=logging.DEBUG, filename='py_log.log',filemode='w', format='%(asctime)s %(levelname)s %(message)s')


def equations(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        logging.warning('discriminant < 0, уравнение не имеет корней')
        raise ValueError('Дискриминант отрицателен, уравнение не имеет корней')

    elif discriminant == 0:
        logging.warning('discriminant = 0, один корень')
        x = - b / (2 * a)
        return x

    else:
        x1 = (-b - discriminant ** 0.5) / (2 * a)
        x2 = (-b + discriminant ** 0.5) / (2 * a)
        return x1, x2

while True:
    try:
        a, b, c = map(float, input('Введите коэффициенты для уравнения в формате: a, b, c: ').split())

        result = equations(a, b, c)
        if len(result) > 1:
            print(f'x1 = {result[0]}, x2 = {result[1]}')
        else:
            print(f'Корень уравнения: x = {result}')
        break

    except ValueError as e:
        logging.warning('discriminant < 0, уравнение не имеет корней')
        print(f'Ошибка: {e}. Попробуйте другие коэффициенты.')
