def factorial(n):
    if n<0:
        return "factorial is not possible with negative values"
    elif n==0 or n==1:
        return "the factorial is 1"    
    else:
        result =1
        for i in range(2,n+1):
            result*=i
        return result
    
number = int(input("Enter a number to find its factorial: "))
print("The factorial of", number, "is", factorial(number))
