import numpy as np

eps = 0.001
max_iter = 1000  # ограничение на число итераций

def task2_1():

    def f1(b, c):
        return (2.18 + 1.65*b + 0.76*c) / 1.53

    def f2(a, c):
        return (1.95 - 0.86*a - 1.84*c) / 1.17

    def f3(a, b):
        return (-0.47 - 0.32*a + 0.65*b) / 1.11

    # ------------------------------
    # Метод Якоби
    # ------------------------------
    def jacobi():
        a = b = c = 0.0
        for iteration in range(1, max_iter+1):
            a_new = f1(b, c)
            b_new = f2(a, c)
            c_new = f3(a, b)

            if max(abs(a_new - a), abs(b_new - b), abs(c_new - c)) < eps:
                return a_new, b_new, c_new, iteration

            a, b, c = a_new, b_new, c_new

        return a, b, c, max_iter

    # ------------------------------
    # Метод Зейделя
    # ------------------------------
    def seidel():
        a = b = c = 0.0
        for iteration in range(1, max_iter+1):
            a_new = f1(b, c)
            b_new = f2(a_new, c)
            c_new = f3(a_new, b_new)

            if max(abs(a_new - a), abs(b_new - b), abs(c_new - c)) < eps:
                return a_new, b_new, c_new, iteration

            a, b, c = a_new, b_new, c_new

        return a, b, c, max_iter

    # ------------------------------
    # Метод Гаусса (прямой)
    # ------------------------------
    def gauss():
        A = np.array([
            [1.53, -1.65, -0.76],
            [0.86, 1.17, 1.84],
            [0.32, -0.65, 1.11]
        ])
        B = np.array([2.18, 1.95, -0.47])
        
        # Решение системы
        X = np.linalg.solve(A, B)
        return X

    # ------------------------------
    # Запуск
    # ------------------------------
    a_j, b_j, c_j, it_j = jacobi()
    a_s, b_s, c_s, it_s = seidel()
    x_gauss = gauss()

    print("Метод Якоби:")
    print(f"a = {a_j:.4f}, b = {b_j:.4f}, c = {c_j:.4f}, итераций = {it_j}")

    print("\nМетод Зейделя:")
    print(f"a = {a_s:.4f}, b = {b_s:.4f}, c = {c_s:.4f}, итераций = {it_s}")

    print("\nМетод Гаусса (точное решение):")
    print(f"a = {x_gauss[0]:.4f}, b = {x_gauss[1]:.4f}, c = {x_gauss[2]:.4f}")
