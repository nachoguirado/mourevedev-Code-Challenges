from retos_python.reto_00 import FizzBuzz

def test_fizzbuzz():
    """
    Test the 'fizzbuzz' method of the FizzBuzz class.

    Scenarios:
    1. When the input is a multiple of 3 but not 5, the method should return "Fizz".
    2. When the input is a multiple of 5 but not 3, the method should return "Buzz".
    3. When the input is a multiple of both 3 and 5, the method should return "Fizzbuzz".
    4. When the input is not a multiple of either 3 or 5, the method should return the string representation of the input.
    """
    fb = FizzBuzz()
    assert fb.fizzbuzz(3) == "Fizz"  # Scenario 1
    assert fb.fizzbuzz(5) == "Buzz"  # Scenario 2
    assert fb.fizzbuzz(15) == "Fizzbuzz"  # Scenario 3
    assert fb.fizzbuzz(11) == "11"  # Scenario 4

def test_number_range():
    """
    Test the 'number_range' method of the FizzBuzz class.

    This test checks the following:
    1. The length of the output list should be 100.
    2. Every item in the output list should be a string.
    3. The output list should match the expected result when the 'fizzbuzz' method is applied to each number in the range 1-100.
    """
    fb = FizzBuzz()
    result = fb.number_range()
    assert len(result) == 100  # Check 1
    assert all(isinstance(x,str) for x in result)  # Check 2
    expected_result = [fb.fizzbuzz(i) for i in range(1,101)]
    assert result == expected_result  # Check 3
