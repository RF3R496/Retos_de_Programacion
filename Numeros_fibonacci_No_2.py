'''
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
'''

def fibonacci_numbers(max_value):
    a = 0
    b = 1

    while a < max_value:
        print(a)
        a,b = b,a+b


if __name__ == '__main__':
    max_value = int(input('ingrese el valor maximo a imprimir\n'))
    fibonacci_numbers(max_value)