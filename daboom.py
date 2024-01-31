import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# input intervals from terminal or in code
# a = int(input())
# b = int(input())
a = -6
a1 = a
b = 6
print(f"input intervals [{a}, {b}]")
# input N from terminal or in code
# n = int(input())
n = 100

print(f"input N = {n}")
# find delta x
dx = (int(b) - int(a)) / n
print(f"{dx} is delta")
print("input function")
# input expression from terminal or in code
# s = input()
s = "sin(e ** x)"
s = s.replace('sin', 'np.sin')
# s = s.replace('e', 'np.e')
s = s.replace('cos', 'np.cos')
s = s.replace('tan', 'np.tan')
s = s.replace('cot', '1 / np.tan')
s = s.replace('e', 'np.e')
s = s.replace('atan', 'np.atan')
s = s.replace('pi', 'np.pi')


print(f"{s}")
func = []
x_val = np.linspace(a1, b)
y_val = [eval(s.replace('x', str(val))) for val in x_val]
plt.plot(x_val, y_val)
plt.savefig('da')
sum1 = 0
while a <= b:
    w = s.replace("x", str(a))
    print(w)
    try:
        result = eval(w)
        func.append(eval(w))
    except ZeroDivisionError:
        print("Error: Division by zero")
    a += dx
for i, e in enumerate(func):
    if i == 0 or i == len(func) - 1:
        sum1 += e
    else:
        sum1 += 2 * e

# print Trapezoidal
T = (dx / 2) * (sum1)

print(f"Trapezoidal is {T}")
sum2 = 0
d = False
for i, e in enumerate(func):
    if i == 0 or i == len(func) - 1:
        sum2 += eval(str(e))
    elif d is False:
        sum2 += 4 * eval(str(e))
        d = True
    elif d is True:
        sum2 += 2 * eval(str(e))
        d = False

# print Simpson
S = (dx / 3) * sum2
x = {'x': Symbol('x', real=True)}
q = s.replace('np.', '')
y = parse_expr(q, x)

# making a graphic
s = s.replace('np.sin', 'sin')
s = s.replace('np.pi', 'pi')
x_val = np.linspace(a1, b, 100)
y_val = [eval(s.replace("x", str(val))) for val in x_val]
# Plotting trapezoids
# Plotting the function
plt.plot(x_val, y_val, label='Function')

# Plotting trapezoids
for i in range(n):
    x_trap = [a1 + i * dx, a1 + (i + 1) * dx, a1 + (i + 1) * dx, a1 + i * dx, a1 + i * dx]
    try:
        y_trap = [0, 0, eval(s.replace("x", str(a1 + (i + 1) * dx))), eval(s.replace("x", str(a1 + i * dx))), 0]
        plt.plot(x_trap, y_trap, 'r-', alpha=0.5)  # Use 'r-' for solid red lines
    except ZeroDivisionError:
        print("Error: Division by zero")

plt.legend()
plt.title("Function and Trapezoids")
plt.xlabel("x")
plt.ylabel("y")

plt.show()


# print som
print(f"By Simpson's Rule S = {S}")
m = diff(y, *2 * [x['x']])  # m that is in E
res2 = []
a = a1
while a1 <= b:
    k = ""
    for i in str(m):
        if i == 'x':
            k += str(a1)
        else:
            k += i
    try:
        res2.append(eval(k))
    except ZeroDivisionError:
        print("div by 0")
    a1 += dx
m = (max(res2))
Et = m * (b - a1) ** 3 / (12 * n ** 2)
print(f"Error estimation is {Et}")

m2 = diff(y, *4 * [x['x']])
res1 = []
while a <= b:
    k = ""
    for i in str(m2):
        if i == 'x':
            k += str(a)
        else:
            k += i
    try:

        res1.append(eval(k))
    except ZeroDivisionError:
        print("div by 0")
    a += dx
m2 = (max(res1))
Es = m2 * ((b - a1) ** 5) / (180 * (n ** 4))
print(f"Error estimation of Simpson's law is {Es}")
