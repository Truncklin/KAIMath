import numpy as np

x_nodes = np.array([0, 2, 3, 5], dtype=float)
f_nodes = 2 ** x_nodes          # f(x) = 2^x
x_star = 1.0                     # точка, где ищем значение

def task3_1():
# ------------------------------
# Полином Лагранжа
# ------------------------------
    def lagrange(x_nodes, f_nodes, x):
        n = len(x_nodes)
        Lx = 0
        for i in range(n):
            term = f_nodes[i]
            for j in range(n):
                if j != i:
                    term *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
            Lx += term
        return Lx

    # ------------------------------
    # Вычисление значения в x_star
    # ------------------------------
    f_interp = lagrange(x_nodes, f_nodes, x_star)
    f_exact = 2 ** x_star            # точное значение
    error = abs(f_exact - f_interp)

    # ------------------------------
    # Вывод результатов
    # ------------------------------
    print(f"Значения функции в узлах: {f_nodes}")
    print(f"Значение полинома Лагранжа в x* = {x_star}: {f_interp:.6f}")
    print(f"Точное значение: {f_exact:.6f}")
    print(f"Оценка погрешности: {error:.6e}")
