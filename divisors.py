#1
def divisor(number):
    """This function returns the number of divisors"""
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
            
number = int(input("Enter any integer to find divisors: "))   
print(f'Divisors of your number are {divisor(number)}')


#2
def divisor(n):
    return [i for i in range(1, n) if n % i == 0]

n = int(input("Enter the number: "))
print(f'The divisors of {n} are: {divisor(n)}')
