import numpy as np
import matplotlib.pyplot as plt
from sympy import *

init_printing(use_unicode=False, wrap_line=False)
# input intervals from terminal or in code
# a = int(input())
# b = int(input())
a = 1
a1 = a
b = 4
jab = a
print(f"input intervals [{a}, {b}]")
# input N from terminal or in code
# n = int(input())
n = 20

print(f"input N = {n}")
# find delta x
dx = (int(b) - int(a)) / n
print(f"{dx} is delta")
print("input function")
# input expression from terminal or in code
# s = input()
s = "sin(x * pi)"
why = s
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

sum1 = 0
while a <= b:
    w = s.replace("x", str(a))
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

S = (dx / 3) * sum2
# print Simpson's quantity
print(f"By Simpson's Rule S = {S}")
x = {'x': Symbol('x', real=True)}
q = s.replace('np.', '')
y = parse_expr(q, x)
s = s.replace('np.sin', 'sin')
s = s.replace('np.pi', 'pi')
s = s.replace('np.cos', 'cos')
s = s.replace('np.tan', 'tan')

# making graphic
# plotting
x_val = np.linspace(a1, b)
y_val = []
for val in x_val:
    w = s.replace("x", str(a))
    try:
        y_val.append(eval(w))
    except ZeroDivisionError:
        print("Error: Division by zero")

plt.plot(x_val, y_val, label=f'{why}', color='black')

# Plotting trapezoids
for i in range(n):
    x_trap = [a1 + i * dx, a1 + (i + 1) * dx, a1 + (i + 1) * dx, a1 + i * dx, a1 + i * dx]
    try:
        y_trap = [0, 0, eval(s.replace("x", str(a1 + (i + 1) * dx))), eval(s.replace("x", str(a1 + i * dx))), 0]
        plt.plot(x_trap, y_trap, 'r-', alpha=0.5, color='red')  # Use 'r-' for solid red lines
    except ZeroDivisionError:
        print("Error: Division by zero")

plt.legend()
plt.title("Function and Trapezoids")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
# Error T
m = diff(y, *2 * [x['x']])  # second derivative
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

m2 = diff(y, *4 * [x['x']])  # 4 derivative

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
print(res1)
Es = m2 * ((b - a1) ** 5) / (180 * (n ** 4))
c1 = integrate(str(y), Symbol('x'))
string1 = str(c1)
string12 = string1.replace('x', f'{jab}')
string2 = string1.replace('x', f'{b}')
print(f"Error estimation of Simpson's law is {Es}")
print("Integral:")
print(eval(string2) - eval(string12))
