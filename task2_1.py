import numpy as np

eps = 0.001
max_iter = 1000
omega = 0.8  # релаксация для метода Зейделя

def task2_1():
    # ------------------------------
    # Система
    # ------------------------------
    A = np.array([
        [0.10, -0.07, -0.96],
        [0.04, -0.99, -0.85],
        [0.91, 1.04, 0.19]
    ])
    B = np.array([-2.04, -3.73, -1.67])

    # ------------------------------
    # Итерационные функции
    # ------------------------------
    def f1(b, c):
        return (-2.04 + 0.07*b + 0.96*c) / 0.10

    def f2(a, c):
        return (-3.73 - 0.04*a + 0.85*c) / -0.99

    def f3(a, b):
        return (-1.67 - 0.91*a - 1.04*b) / 0.19

    # ------------------------------
    # Метод Якоби
    # ------------------------------
    def jacobi(x0):
        a, b, c = x0
        for iteration in range(1, max_iter+1):
            a_new = f1(b, c)
            b_new = f2(a, c)
            c_new = f3(a, b)

            if max(abs(a_new - a), abs(b_new - b), abs(c_new - c)) < eps:
                return a_new, b_new, c_new, iteration

            a, b, c = a_new, b_new, c_new
        return a, b, c, max_iter

    # ------------------------------
    # Метод Зейделя с релаксацией
    # ------------------------------
    def seidel(x0):
        a, b, c = x0
        for iteration in range(1, max_iter+1):
            a_new = omega * f1(b, c) + (1 - omega) * a
            b_new = omega * f2(a_new, c) + (1 - omega) * b
            c_new = omega * f3(a_new, b_new) + (1 - omega) * c

            if max(abs(a_new - a), abs(b_new - b), abs(c_new - c)) < eps:
                return a_new, b_new, c_new, iteration

            a, b, c = a_new, b_new, c_new
        return a, b, c, max_iter

    # ------------------------------
    # Метод Гаусса (точный)
    # ------------------------------
    def gauss():
        X = np.linalg.solve(A, B)
        return X

    # ------------------------------
    # Начальное приближение из метода Гаусса
    # ------------------------------
    x0 = gauss()

    # ------------------------------
    # Запуск методов
    # ------------------------------
    a_j, b_j, c_j, it_j = jacobi(x0)
    a_s, b_s, c_s, it_s = seidel(x0)
    x_gauss = gauss()

    print("Метод Якоби:")
    print(f"a = {a_j:.4f}, b = {b_j:.4f}, c = {c_j:.4f}, итераций = {it_j}")

    print("\nМетод Зейделя (с релаксацией):")
    print(f"a = {a_s:.4f}, b = {b_s:.4f}, c = {c_s:.4f}, итераций = {it_s}")

    print("\nМетод Гаусса (точное решение):")
    print(f"a = {x_gauss[0]:.4f}, b = {x_gauss[1]:.4f}, c = {x_gauss[2]:.4f}")