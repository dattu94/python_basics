number = int(input("Enter the number to know if the number is prime or composite: "))

def prime(a):
    if a < 2:
        print('The number is neither prime nor composite')
        return

    for i in range(2, int(a * 0.5) + 1):
        if a % i == 0:
            print(f"The number {a} is a composite number")
            return

    print(f"The number {a} is a prime number")

prime(number)


