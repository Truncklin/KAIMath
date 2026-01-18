import numpy as np
import matplotlib.pyplot as plt

def task1():
    def f(x):
        return 1 + np.exp(x) - 2/x


    x = np.linspace(0, 4, 400)
    y = f(x)

    plt.figure()
    plt.axhline(0)          # ось X
    plt.plot(x, y)
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("График функции f(x)")
    plt.show()


    a = 0.0       
    b = 1.0       
    eps = 0.001   

    iteration = 0

    while abs(b - a) > eps:
        x_mid = (a + b) / 2

        if f(a) * f(x_mid) < 0:
            b = x_mid
        else:
            a = x_mid

        iteration += 1

    root = (a + b) / 2

    print("Метод половинного деления")
    print("Количество итераций:", iteration)
    print("Приближённый корень:", root)
