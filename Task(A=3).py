#Task 1 factorial(n):
def factorial(n):
    result=1
    for i in range(1, n +1):
        result *= i
    return result

#Input from user
num = int(input(" enter the number: "))
print(f"Factorial of {num} is:{factorial(num)}")