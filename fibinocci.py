def fibonacci_series_using_ab(n):
    """
    Generate the Fibonacci series up to the nth term using two variables a and b.
    :param n: Number of terms in the Fibonacci series
    :return: List containing the Fibonacci series
    """
    series = []
    a, b = 0, 1  # Initialize the first two terms
    
    for _ in range(n):
        series.append(a)  # Add the current value of a to the series
        a, b = b, a + b  # Update a and b for the next Fibonacci number
    
    return series

# Example Usage
num_terms = int(input("Enter the number of terms: "))
print(f"Fibonacci series (first {num_terms} terms): {fibonacci_series_using_ab(num_terms)}")
10