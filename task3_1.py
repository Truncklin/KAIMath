import numpy as np

# ------------------------------
# Узлы и значения функции
# ------------------------------
x_nodes = np.array([1.0, 2.0, 2.5, 3.0], dtype=float)
f_nodes = np.log(x_nodes)        # f(x) = ln(x)
x_star = 1.5                     # точка, где ищем значение

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
    f_exact = np.log(x_star)       # точное значение
    error = abs(f_exact - f_interp)

    # ------------------------------
    # Вывод результатов
    # ------------------------------
    print(f"Значения функции в узлах: {np.round(f_nodes, 6)}")
    print(f"Значение полинома Лагранжа в x* = {x_star}: {f_interp:.6f}")
    print(f"Точное значение: {f_exact:.6f}")
    print(f"Оценка погрешности: {error:.6e}")
