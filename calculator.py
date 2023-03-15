import math
import re
from pythonds.basic import Stack

output = []
ch = Stack()
precedence = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.b - self.a

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

    def power(self):
        return pow(self.a, self.b)

    def sin(self):
        return math.sin(math.radians(self.a))

    def cosine(self):
        return math.cos(math.radians(self.a))

    def tan(self):
        return math.tan(math.radians(self.a))

    def secant(self):
        return math.acos(math.radians(self.a))

    def cosecant(self):
        return math.asin(math.radians(self.a))

    def cotangent(self):
        return math.atan(math.radians(self.a))


def postfix(exp):  # Postfix function
    for i in exp:
        if i == '(':
            ch.push(i)
        elif i == ')':
            while ch.peek() != '(':
                x = ch.pop()
                output.append(x)
            ch.pop()
        elif i == '*' or i == '/' or i == '+' or i == '-' or i == '^':
            if not ch.isEmpty():
                while precedence[ch.peek()] >= precedence[i]:
                    ele = ch.pop()
                    output.append(ele)
                    if ch.isEmpty:
                        break
                ch.push(i)
            if ch.isEmpty() or ch.peek() == '(':
                ch.push(i)
        else:
            output.append(i)
    while not ch.isEmpty():
        a = ch.pop()
        output.append(a)
    for j in output:
        print(j, end='')
    q = ' '.join(output)
    evaluation(q)

    return q


def evaluation(q):  # evaluation
    output2 = []
    d = q.split(' ')
    chh = Stack()
    chh.isEmpty()
    for ev in d:
        if ev == '*' or ev == '/' or ev == '+' or ev == '-' or ev == '^':
            a1 = chh.pop()
            a = float(a1)
            b1 = chh.pop()
            b = float(b1)
            if ev == '*':
                result = b * a
                chh.push(result)
                chh.pop()
            if ev == '+':
                result = b + a
                chh.push(result)
                chh.pop()
            if ev == '/':
                result = b / a
                chh.push(result)
                chh.pop()
            if ev == '-':
                result = b - a
                chh.push(result)
                chh.pop()
            chh.push(result)
        else:
            chh.push(ev)
            output2.append(ev)

    print("\nThe Answer is:", chh.pop())

a = int(input("enter number1: "))  # Calculator class
b = int(input("enter number2: "))
obj = Calculator(a, b)

while True:
    x = '1. Add \n2. Subtract  \n3. Multiply  \n4. Divide  \n5. Exponent  \n6. Sin  \n7. Cos  \n8. Tan \n9. Sec ' \
        '\n10. Cosec  \n11. Cot  \n0. Quit'
    print(x)
    choice = int(input('Please select from 0 to 10 : '))
    if choice == 1:
        print("\nResult of Addition = ", obj.add())
    elif choice == 2:
        print("\nResult of Subtraction = ", obj.subtract())
    elif choice == 3:
        print("\nResult of multiplication = ", obj.multiply())
    elif choice == 4:
        print("\nResult of division = ", obj.divide())
    elif choice == 5:
        print("\nResult = ", obj.power())
    elif choice == 6:
        print(f"\nSin({a})={obj.sin()}")
    elif choice == 7:
        print(f"\nCos({a})={obj.cosine()}")
    elif choice == 8:
        print(f"\nTan({a})={obj.tan()}")
    elif choice == 9:
        print(f"\nSec({a})={obj.secant()}")
    elif choice == 10:
        print(f"\nCosec({a})={obj.cosecant()}")
    elif choice == 11:
        print(f"\nCot({a})={obj.cotangent()}")
    elif choice == 0:
        break
    else:
        print('Invalid option')
        break

exp = input('Enter expression: ')
values = re.findall(r"(\d+|[-+()/*])", exp)
w = postfix(values)
