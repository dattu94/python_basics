'''Lambda function takes arugemts and the function.
It is a anonymous function
syntax --> lambda arguments: expression with arguments
example: add = lambda x,y: x+y'''

add = lambda x,y: x+y

res =add(3,4)
print(res)

"example of lambda function with filter"

l1 = [1,2,3,6,8,10,12]

even_num = list(filter(lambda x: x%2 ==0,l1))
print(even_num)

'''example of lambda function with map
The map() function applies a given function to all items in an iterable (like a list) and
returns a map object (which can be converted to a list, tuple, etc.)

syntax: -->
map(function, iterable, *iterables)'''

div_by3 = list(map(lambda X: X/3, l1))
print(div_by3)

nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums)) 
print(squared)

'''
the enumerate() function used to iterate over the sequence while keeping the trak of index
adds a counter to an iterable and returns it as an enumerating object.


syntax:--> enumerate(iterable, start= 0)
the start will ierate the index number'''


# Example: Using enumerate to iterate with an index
fruits = ["apple", "banana", "cherry", "date"]
print("Enumerating fruits:")
for index, fruit in enumerate(fruits, start =2):
    print(f"{index}: {fruit}")
