# This is a calculator using only two operands
def addition(x, y):
    print(x, "+", y, "=", x + y)


def minus(x, y):
    print(x, "-", y, "=", x - y)


def multiply(x, y):
    print(x, "*", y, "=", x * y)


def division(x, y):
    print(x, "/", y, "=", x / y)


def avg(x, y):
    print("average of", x, "and", y, "=", (x + y) / 2)


x = float(input("Enter the 1st number"))
y = float(input("Enter the 2nd number"))

print("Select Operation from the following")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Average")
print("6.All Operations")

ch = int(input())

if ch == 1:
    addition(x, y)

elif ch == 2:
    minus(x, y)

elif ch == 3:
    multiply(x, y)

elif ch == 4:
    division(x, y)

elif ch == 5:
    avg(x, y)

elif ch == 6:
    addition(x, y)
    minus(x, y)
    multiply(x, y)
    division(x, y)
    avg(x, y)
else:
    print("check your input")
