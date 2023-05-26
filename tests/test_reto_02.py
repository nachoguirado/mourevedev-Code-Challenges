from retos_python.reto_02 import Fibonacci

def test_fibonacci_serie():
    """
    Test the `fibonacci_serie` method of the `Fibonacci` class.
    
    This test covers four different scenarios:
    1. Testing with 0, the smallest possible input, to confirm that the base case of the Fibonacci sequence is handled correctly.
    2. Testing with 10, a small positive number, to check that the function computes the correct value for inputs in the middle of the sequence.
    3. Testing with 20, a larger positive number, to verify that the function can accurately compute values later in the sequence.
    4. Testing with 25, an even larger number, to ensure that the function remains accurate for inputs at the higher end of the sequence.
    """
    obj = Fibonacci()
    
    # Scenario 1: Base case
    assert obj.fibonacci_serie(0) == 0

    # Scenario 2: Small positive input
    assert obj.fibonacci_serie(10) == 55

    # Scenario 3: Larger positive input
    assert obj.fibonacci_serie(20) == 6765

    # Scenario 4: High positive input
    assert obj.fibonacci_serie(25) == 75025
