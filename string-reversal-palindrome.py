
'''You can reverse a string without using built-in functions by iterating through the string in reverse order and constructing a new string. Here’s how you can do it:

Program to Reverse a String Without Built-in Functions
python
Copy code'''
def reverse_string(s):
    """
    Reverse a string without using built-in functions.
    :param s: The input string
    :return: The reversed string
    """
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):  # Iterate from the last index to the first
        reversed_str += s[i]  # Append characters to the result
    return reversed_str

# Example Usage
input_string = input("Enter a string to reverse: ")
print(f"Reversed string: {reverse_string(input_string)}")