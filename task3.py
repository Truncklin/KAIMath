import numpy as np

def task3():
    def f(x):
        return x**3 - 12*x + 4

    def chord_method(x0, x1, eps=0.001):
        iteration = 0
        while abs(x1 - x0) > eps:
            x_new = x1 - f(x1)*(x1 - x0)/(f(x1)-f(x0))
            x0, x1 = x1, x_new
            iteration += 1
        return x1, iteration

    def false_position(xa, xb, eps=0.001):
        iteration = 0
        while True:
            xr = xb - f(xb)*(xb - xa)/(f(xb)-f(xa))
            iteration += 1
            if abs(f(xr)) < eps:
                return xr, iteration
            if f(xr)*f(xa) < 0:
                xb = xr
            else:
                xa = xr

    intervals = [(-4, -3), (0, 1), (3, 4)]

    print("Метод хорд:")
    for x0, x1 in intervals:
        root, it = chord_method(x0, x1)
        print(f"Корень в интервале [{x0},{x1}] -> {root:.4f}, итераций = {it}")

    print("\nМетод ложного положения:")
    for xa, xb in intervals:
        root, it = false_position(xa, xb)
        print(f"Корень в интервале [{xa},{xb}] -> {root:.4f}, итераций = {it}")
