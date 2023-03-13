import numpy as np
import math


class Calculator:
    def add(self):
        n = int(input("enter total numbers to add: "))
        sum1 = 0
        for i in range(1, n + 1):
            num = input(f'enter number {i}: ')
            sum1 = sum1 + i
        print("Result of Addition: ", sum1)


    def subtract(self):
        print("\n Subtraction")
        num1 = int(input("enter number1: "))
        num2 = int(input("enter number2: "))
        diff = np.subtract(num1, num2)
        print("Result of Subtraction: ", diff)

    def multiply(self):
        print("\n Multiply")
        num1 = int(input("enter number1: "))
        num2 = int(input("enter number2: "))
        mul = np.multiply(num1, num2)
        print("Result of Multiplication: ", mul)

    def divide(self):
        print("\n Division")
        num1 = int(input("enter number1: "))
        num2 = int(input("enter number2: "))
        div = np.divide(num1, num2)
        print("Result of Division: ", div)

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




a = Calculator()
a.add()
a.subtract()
a.multiply()
a.divide()
a.sin()
a.cosine()
a.tan()
a.secant()
a.secant()
a.cosecant()
a.cotangent()


# postfix code


class evalpostfix:
	def __init__(self):
		self.stack =[]
		self.top =-1
	def pop(self):
		if self.top ==-1:
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
				    switcher = {'+':val2 + val1, '-':val2-val1, '*':val2 * val1, '^':val2**val1}
				    self.push(switcher.get(i))
		return int(self.pop())

str ='200 100 - 12 / 35 - 97 +'

strconv = str.split(' ')
obj = evalpostfix()
print(obj.centralfunc(strconv))




