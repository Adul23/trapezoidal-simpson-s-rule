
import numpy as np
import matplotlib.pyplot as plt
from sympy import *


# input intervals from terminal or in code
# a = int(input())
# b = int(input())
a = 2
a1 = a
b = 4
print(f"input intervals [{a}, {b}]")
# input N from terminal or in code
# n = int(input())
n = 4

print(f"input N = {n}")
# find delta x
dx = (int(b) - int(a)) / n
print(f"{dx} is delta")
print("input function")
# input expression from terminal or in code
# s = input()
s = "log(x) * cos(x) * pi *pi"
print(f"{s}")
func = []
x_val = np.linspace(a1, b)
y_val = [eval(s.replace('x', str(val))) for val in x_val]
plt.plot(x_val, y_val)
sum1 = 0
while a <= b:
    w = s.replace("x", str(a))
    func.append(eval(w))
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
        sum2 += e
    elif d is False:
        sum2 += 4 * e
        d = True
    elif d is True:
        sum2 += 2 * e
        d = False
# print Simpson
S = (dx / 3) * sum2
x = {'x': Symbol('x', real=True)}
y = parse_expr(s, x)

# making a graphic

x_val = np.linspace(a1, b, 100)
y_val = [eval(s.replace("x", str(val))) for val in x_val]
plt.plot(x_val, y_val)

# Plotting trapezoids
for i in range(n):

    x_trap = [a1 + i * dx, a1 + (i + 1) * dx, a1 + (i + 1) * dx, a1 + i * dx, a1 + i * dx]
    y_trap = [0, 0, eval(s.replace("x", str(a1 + (i + 1) * dx))), eval(s.replace("x", str(a1 + i * dx))), 0]
    print(x_trap, y_trap)
    plt.plot(x_trap, y_trap, 'r--')
plt.legend()
plt.title("Function and Trapezoids")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
# print som
print(f"By Simpson's Rule S = {S}")
m = diff(y, *2 * [x['x']])  # m that is in E
# plt.show()
res2 = []
for j in range(a1, b + 1):
    k = ""
    for i in str(m):
        if i == 'x':
            k += str(j)
        else:
            k += i
    res2.append(eval(k))
m = (max(res2))
Et = m * (b - a1) ** 3 / (12 * n ** 2)
# print(m)
print(f"Error estimation is {Et}")
m2 = diff(y, *4 * [x['x']])
res1 = []
for j in range(a1, b + 1):
    k = ""
    for i in str(m2):
        if i == 'x':
            k += str(j)
        else:
            k += i
    res1.append(eval(k))
m2 = (max(res1))
Es = m2 * ((b - a1) ** 5) / (180 * (n ** 4))
print(f"Error estimation of Simpson's law is {Es}")
