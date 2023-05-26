'''/*
 * Reto #2
 * LA SUCESIÓN DE FIBONACCI
 * Fecha publicación enunciado: 10/01/22
 * Fecha publicación resolución: 17/01/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
 * La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
 * 0, 1, 1, 2, 3, 5, 8, 13...
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */'''
"""
Here there are several ways to solve the problem. The recursive way, the fibonnaci matrix, etc... Since the recursive way would lead us to an exponential execution time O(2^n).
I have chosen iteration for its efficiency, since it allows us to have a logarithmic runtime O(n). 
"""
class Fibonacci:
    """
    This class is used to calculate the Fibonacci series.
    
    The Fibonacci series is a sequence of numbers where the next number is found by adding up the two numbers before it.
    The sequence looks like this: 0, 1, 1, 2, 3, 5, 8, 13, etc
    """
    def fibonacci_serie(self, n:int) -> int:
        """
        Calculate the nth number in the Fibonacci series using an iterative method.

        Parameters:
        n (int): The position in the Fibonacci series to calculate. n should be a non-negative integer.

        Returns:
        int: The nth number in the Fibonacci series.
        """
        if n < 2:
            return n
        else:
            a, b = 0, 1
            for _ in range(n-1):
                a, b = b, a + b
            return b

obj = Fibonacci()
for x in range(51):
    print(obj.fibonacci_serie(x))
