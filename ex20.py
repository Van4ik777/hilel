import unittest


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]

def formatted_name(first_name, last_name, middle_name=''):
   if len(middle_name) > 0:
       full_name = first_name + ' ' + middle_name + ' ' + last_name
   else:
       full_name = first_name + ' ' + last_name
   return full_name.title()

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_fibonacci_function(self):
        self.assertEqual(self.fibonacci(0), 0)  
        self.assertEqual(self.fibonacci(1), 1)  

    def test_fibonacci_recursive(self):
        self.assertEqual(self.fibonacci(5), 5)  
        self.assertEqual(self.fibonacci(10), 55)  

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci(-1)  
        with self.assertRaises(ValueError):
            self.fibonacci("string")

class TestFormattedName(unittest.TestCase):
    def test_full_name_with_middle_name(self):
        self.assertEqual(formatted_name("John", "Doe", "Michael"), "John Michael Doe")

    def test_full_name_with_lastname(self):
        self.assertEqual(formatted_name("John", "Doe"), "John Doe")

    def test_name_speling(self):
        self.assertEqual(formatted_name("john", "doe", "michael"), "John Michael Doe")