import math
import numpy as np


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        n = int(input("enter total numbers to add: "))
        sum1 = 0
        for i in range(1, n + 1):
            num = input(f'enter number {i}: ')
            sum1 = sum1 + i
        print("Result of Addition: ", sum1)

    def subtract(self):
        print("\n Subtraction")
        return self.b - self.a

    def multiply(self):
        print("\n Multiply")
        return self.a * self.b

    def divide(self):
        print("\n Division")
        return self.a / self.b

    def power(self):
        print("\n Exponent")
        return pow(self.a, self.b)

    def sin(self):
        print("\n Sin")
        n = int(input("enter number: "))
        res = math.radians(n)
        result = math.sin(res)
        print(f"Sin({n})={result}")

    def cosine(self):
        print("\n Cosine")
        n = int(input("enter number: "))
        res = math.radians(n)
        result = math.cos(res)
        print(f"Cos({n})={result}")

    def tan(self):
        print("\n Tangent")
        n = int(input("enter number: "))
        res = math.radians(n)
        result = math.tan(res)
        print(f"Tan({n})={result}")

    def secant(self):
        print("\n Secant")
        n = int(input("enter number: "))
        res = math.radians(n)
        result = math.acos(res)
        print(f"Sec({n})={result}")

    def cosecant(self):
        print("\n Cosecant")
        n = int(input("enter number: "))
        res = math.radians(n)
        result = math.asin(res)
        print(f"Cosc({n})={result}")

    def cotangent(self):
        print("\n Cotangent")
        n = int(input("enter number: "))
        res = math.radians(n)
        result = math.atan(res)
        print(f"Tan({n})={result}")


class Evalpostfix:
    def __init__(self):
        self.stack = []
        self.top = -1

    def pop(self):
        if self.top == -1:
            return
        else:
            self.top = self.top - 1
            return self.stack.pop()

    def push(self, i):
        self.top = self.top + 1
        self.stack.append(i)

    def centralfunc(self, ab):
        for i in ab:
            try:
                self.push(int(i))
            except ValueError:
                val1 = self.pop()
                val2 = self.pop()

                if i == '/':
                    self.push(val2 / val1)
                else:
                    switcher = {'+': val2 + val1, '-': val2 - val1, '*': val2 * val1, '^': val2 ** val1}
                    self.push(switcher.get(i))
        return int(self.pop())


a = int(input("enter number1: "))
b = int(input("enter number2: "))
obj = Calculator(a, b)

while True:
    x = '1. Add \n2. Subtract  \n3. Multiply  \n4. Divide  \n5. Exponent  \n6. Sin  \n7. Cos  \n8. Tan \n9. Sec ' \
        '\n10. Cosec  \n11. Cot  \n0. Quit'
    print(x)
    choice = int(input('Please select from 0 to 10 : '))
    if choice == 1:
        obj.add()
    elif choice == 2:
        print("Result = ", obj.subtract())
    elif choice == 3:
        print("Result = ", obj.multiply())
    elif choice == 4:
        print("Result = ", obj.divide())
    elif choice == 5:
        print("Result = ", obj.power())
    elif choice == 6:
        obj.sin()
    elif choice == 7:
        obj.cosine()
    elif choice == 8:
        obj.tan()
    elif choice == 9:
        obj.secant()
    elif choice == 10:
        obj.cosecant()
    elif choice == 11:
        obj.cotangent()
    elif choice == 0:
        break
    else:
        print('Invalid option')
        break

string = '200 100 - 12 / 35 - 97 +'
strconv = string.split(' ')
obj1 = Evalpostfix()
print("\nResult of given infix expression to postfix:")
print(obj1.centralfunc(strconv))
