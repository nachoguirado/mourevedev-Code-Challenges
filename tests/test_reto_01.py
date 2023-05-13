from retos_python.reto_01 import AnagramWord

def test_is_anagram_or_not():
    """
    Test the 'is_anagram_or_not' method of the AnagramWord class. 
    This test checks two scenarios: 
    1. When the words are anagrams of each other, the method should return True.
    2. When the words are not anagrams of each other, the method should return False.
    """
    word_01 = 'hola'
    word_02 = 'loha'
    word_03 = 'chau'
    
    # Scenario 1, the words are anagrams
    anagram_test_01 = AnagramWord(word_01,word_02)
    assert anagram_test_01.is_anagram_or_not() == True
    
    # Scenario 2, the words are not anagrams
    anagram_test_02 = AnagramWord(word_01,word_03)
    assert anagram_test_02.is_anagram_or_not() == False
 