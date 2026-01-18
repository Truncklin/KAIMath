def task2():
    def f(x):
        return x**3 - 6*x - 8

    def df(x):
        return 3*x**2 - 6

    # ---------- Метод касательных (Ньютона) ----------
    def newton(x0, eps=0.001):
        x = x0
        it = 0
        while True:
            x_new = x - f(x) / df(x)
            it += 1
            if abs(x_new - x) < eps:
                return x_new, it
            x = x_new

    # ---------- Метод простых итераций ----------
    def simple_iter(x0, eps=0.001):
        x = x0
        it = 0
        while True:
            x_new = (6*x + 8)**(1/3)
            it += 1
            if abs(x_new - x) < eps:
                return x_new, it
            x = x_new

    # ===== Первый корень =====
    x0_1 = -2.5
    root_n1, it_n1 = newton(x0_1)
    root_i1, it_i1 = simple_iter(x0_1)

    # ===== Второй корень =====
    x0_2 = 2.5
    root_n2, it_n2 = newton(x0_2)
    root_i2, it_i2 = simple_iter(x0_2)

    print("Первый корень:")
    print(f"Метод касательных: x = {root_n1:.4f}, итераций = {it_n1}")
    print(f"Метод простых итераций: x = {root_i1:.4f}, итераций = {it_i1}")

    print("\nВторой корень:")
    print(f"Метод касательных: x = {root_n2:.4f}, итераций = {it_n2}")
    print(f"Метод простых итераций: x = {root_i2:.4f}, итераций = {it_i2}")
