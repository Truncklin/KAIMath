import numpy as np


x_nodes = np.array([1, 3, 5, 7, 9], dtype=float)
f_nodes = np.log(x_nodes)       # f(x) = ln(x)
x_star = 4.0

def task3_3():
    def divided_differences(x, y):
        n = len(x)
        coef = np.copy(y)
        for j in range(1, n):
            for i in range(n-1, j-1, -1):
                coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
        return coef

    # ------------------------------
    # Полином Ньютона
    # ------------------------------
    def newton_poly(x_nodes, coef, x):
        n = len(coef)
        result = coef[0]
        product = 1.0
        for i in range(1, n):
            product *= (x - x_nodes[i-1])
            result += coef[i] * product
        return result

    # ------------------------------
    # Расчёт
    # ------------------------------
    coef = divided_differences(x_nodes, f_nodes)
    f_interp = newton_poly(x_nodes, coef, x_star)

    # Точное значение и погрешность
    f_exact = np.log(x_star)
    error = abs(f_exact - f_interp)

    # ------------------------------
    # Вывод результатов
    # ------------------------------
    print("Коэффициенты разделённых разностей:", np.round(coef, 6))
    print(f"Значение полинома Ньютона в x* = {x_star}: {f_interp:.6f}")
    print(f"Точное значение: {f_exact:.6f}")
    print(f"Оценка погрешности: {error:.6e}")
