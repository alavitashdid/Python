import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')

user_input = input("関数 f(x) を入力してください: f(x) = ")

try:
    user_input = user_input.replace("e", "E")
    expr = sp.sympify(user_input)
except Exception as e:
    print("数式として認識できませんでした:", e)
    exit()

xmin, xmax = -10, 10
ymin, ymax = -10, 10

f = sp.lambdify(x, expr, "numpy")

xs = np.linspace(xmin, xmax, 1000)

try:
    ys = f(xs)
    if np.isscalar(ys):
        ys = np.full_like(xs, ys)
    elif isinstance(ys, np.ndarray) and ys.ndim == 0:
        ys = np.full_like(xs, ys.item())
except Exception as e:
    print("関数を評価できませんでした:", e)
    exit()

plt.plot(xs, ys)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title(f"f(x) = {user_input}")
plt.grid(True)

plt.ylim(ymin, ymax)
plt.gca().set_aspect('equal', adjustable='box')

plt.show()
