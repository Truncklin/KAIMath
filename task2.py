def task2():
    def f(x):
        return 2*x**3 - 9*x**2 - 3*x + 2

    def df(x):
        return 6*x**2 - 18*x - 3

    # -------- Метод касательных --------
    def tangent(x0, eps=0.001):
        x = x0
        it = 0
        while True:
            x_new = x - f(x)/df(x)
            it += 1
            if abs(x_new - x) < eps:
                return x_new, it
            x = x_new

    # -------- Метод простых итераций --------
    def simple_iter(x0, eps=0.001):
        x = x0
        it = 0
        while True:
            x_new = (9*x**2 + 3*x - 2)/(2*x**2)
            it += 1
            if abs(x_new - x) < eps:
                return x_new, it
            x = x_new

    # ====== Первый корень ======
    x0_1 = 0.3
    r1_t, it1_t = tangent(x0_1)
    r1_i, it1_i = simple_iter(x0_1)

    # ====== Второй корень ======
    x0_2 = 5.0
    r2_t, it2_t = tangent(x0_2)
    r2_i, it2_i = simple_iter(x0_2)

    print("Первый корень:")
    print(f"Метод касательных: x = {r1_t:.4f}, итераций = {it1_t}")
    print(f"Метод простых итераций: x = {r1_i:.4f}, итераций = {it1_i}")

    print("\nВторой корень:")
    print(f"Метод касательных: x = {r2_t:.4f}, итераций = {it2_t}")
    print(f"Метод простых итераций: x = {r2_i:.4f}, итераций = {it2_i}")
