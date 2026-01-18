def task3():
    def f(x):
        return 2*x**4 - x**2 - 10

    # -------- Метод хорд --------
    def chord(x0, x1, eps=0.001):
        it = 0
        while abs(x1 - x0) > eps:
            x_new = x1 - f(x1)*(x1 - x0)/(f(x1)-f(x0))
            x0, x1 = x1, x_new
            it += 1
        return x1, it

    # -------- Метод ложного положения --------
    def false_position(a, b, eps=0.001):
        it = 0
        while True:
            x = b - f(b)*(b - a)/(f(b)-f(a))
            it += 1
            if abs(f(x)) < eps:
                return x, it
            if f(a)*f(x) < 0:
                b = x
            else:
                a = x

    intervals = [(-3, -2), (2, 3)]

    print("Метод хорд:")
    for a, b in intervals:
        r, it = chord(a, b)
        print(f"[{a}, {b}] → x = {r:.4f}, итераций = {it}")

    print("\nМетод ложного положения:")
    for a, b in intervals:
        r, it = false_position(a, b)
        print(f"[{a}, {b}] → x = {r:.4f}, итераций = {it}")
