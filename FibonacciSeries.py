# Getting all the fibonacci numbers till 'n'


def fib(n):
    first = 0
    second = 1
    if n == 1:
        print(first)
    else:
        print(first)
        print(second)
        for i in range(2, n):
            next = first + second
            first = second
            second = next
            print(next)


n = int(input("Enter how many numbers in fibonacci series to display"))
if n <= 0:
    print("Invalid Input")
else:
    fib(n)
