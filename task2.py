def task2():
    def f(x):
        return x**3 - 6*x - 8

    def df(x):
        return 3*x**2 - 6

    def newton(x0, eps=0.001):
        x = x0
        iteration = 0
        while True:
            x_new = x - f(x)/df(x)
            iteration += 1
            if abs(x_new - x) < eps:
                break
            x = x_new
        return x_new, iteration

    def simple_iter(x0, eps=0.001):
        x = x0
        iteration = 0
        while True:
            x_new = (6*x + 8)**(1/3)
            iteration += 1
            if abs(x_new - x) < eps:
                break
            x = x_new
        return x_new, iteration

    x0 = 2.5
    root_newton, it_newton = newton(x0)
    root_iter, it_iter = simple_iter(x0)

    print("Метод Ньютона:")
    print(f"Корень = {root_newton:.4f}, итераций = {it_newton}")

    print("Метод простых итераций:")
    print(f"Корень = {root_iter:.4f}, итераций = {it_iter}")
