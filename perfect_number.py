#1
def is_perfect(n:int):
    """This function shows if the number is perfect"""
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n 
        
n = int(input("Enter your number: "))        
print(is_perfect(n))
