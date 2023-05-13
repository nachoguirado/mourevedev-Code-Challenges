'''/*
 * Reto #1
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 10/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean)
 según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, 
 dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución 
 aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */'''
 

class AnagramWord:
    
    def __init__(self, word_01:str, word_02:str):
        self.word_01 = list(word_01.lower())
        self.word_02 = list(word_02.lower())
        
    def is_anagram_or_not(self)-> bool:
        
        """Check if two words are anagrams.

        This function takes two words and determines whether they are anagrams of each other.
        An anagram is a word or phrase formed by rearranging the letters of another word or phrase.
        The function sorts the letters of both words and checks if the sorted lists are equal.

        Args:
            self (object): The instance of the class containing the two words to be checked.

        Returns:
            bool: True if the words are anagrams, False otherwise.
        """
                 
        list_01 = sorted(self.word_01)
        list_02 = sorted(self.word_02)
        
        if list_01 == list_02:
            print("Es un anagrama")
            return True
        else:
            print("No es un anagrama")
            return False
            
