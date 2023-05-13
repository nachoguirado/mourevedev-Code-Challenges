'''
/*
 * Reto #0
 * EL FAMOSO "FIZZ BUZZ"
 * Fecha publicación enunciado: 27/12/21
 * Fecha publicación resolución: 03/01/22
 * Dificultad: FÁCIL
 * Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */'''

class FizzBuzz:
    """
    The FizzBuzz class implements the FizzBuzz game.
    """

    def fizzbuzz(self, value:int) -> str:
        """
        Returns 'Fizz' if the value is divisible by 3, 'Buzz' if it's divisible by 5, 
        and 'FizzBuzz' if it's divisible by both 3 and 5. If the value is not divisible
        by 3 or 5, it returns the value as a string.
        
        Parameters:
        value (int): The number to evaluate.
        
        Returns:
        str: The result of the FizzBuzz evaluation.
        """
        if value % 3 == 0 and value % 5 == 0:
            return "Fizzbuzz"
        elif value % 3 == 0:
            return "Fizz"
        elif value % 5 == 0:
            return "Buzz"
        else:
            return str(value)

    def number_range(self) -> list:
        """
        Prints and returns a list of FizzBuzz results for the numbers from 1 to 100.

        Returns:
        list: The list of FizzBuzz results.
        """
        results = []
        for i in range(1, 101):
            result = self.fizzbuzz(value=i)            
            print(result)
            print("\n")
            results.append(result)
        return results   