import math
import re

# from pythonds.basic import Stack

output = []
operator = []
precedence = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
operators = ['+', '-', '*', '/', '^']
output2 = []
operator1 = []


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


def postfix(exp):

    for i in exp:

        if i == '(':
            operator.append(i)
        elif i == ')':

            while operator[-1] != '(':

                x = operator.pop()
                output.append(x)
            operator.pop()
        elif i in operators:
            if len(operator) != 0:

                while precedence[operator[-1]] >= precedence[i]:

                    ele = operator.pop()
                    output.append(ele)
                    if len(operator) == 0:
                        break

                operator.append(i)

            if len(operator) == 0 or operator[-1] == '(':
                operator.append(i)
        else:
            output.append(i)

    while len(operator) != 0:

        a = operator.pop()
        output.append(a)

    for j in output:

        print(j, end='')
    q = ' '.join(output)
    evaluation(q)

    return q


# evaluation

def evaluation(q):
    output2 = []
    d = q.split(' ')

    for ev in d:

        if ev in operators:
            a1 = operator1.pop()
            a = float(a1)
            b1 = operator1.pop()
            b = float(b1)
            if ev in operators[2]:
                result = a.__mul__(b)
                operator1.append(result)
                operator1.pop()
            if ev in operators[0]:
                result = a.__add__(b)
                operator1.append(result)
                operator1.pop()
            if ev in operators[-2]:
                result = a.__divmod__(b)
                operator1.append(result)
                operator1.pop()
            if ev in operators[1]:
                result = a.__sub__(b)
                operator1.append(result)
                operator1.pop()
            operator1.append(result)
        else:
            operator1.append(ev)
            output2.append(ev)

    print("\nThe Answer is:", operator1.pop())


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
