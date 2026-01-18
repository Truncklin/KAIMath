import numpy as np

eps = 0.001
max_iter = 1000

# ------------------------------
# Итерационные функции
# ------------------------------
def f1(b, c):
    # a = (-2.04 + 0.07b + 0.96c) / 0.10
    return (-2.04 + 0.07*b + 0.96*c) / 0.10

def f2(a, c):
    # b = (-3.73 - 0.04a + 0.85c) / -0.99
    return (-3.73 - 0.04*a + 0.85*c) / -0.99

def f3(a, b):
    # c = (-1.67 - 0.91a - 1.04b) / 0.19
    return (-1.67 - 0.91*a - 1.04*b) / 0.19

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
# Метод Гаусса (точный)
# ------------------------------
def gauss():
    A = np.array([
        [0.10, -0.07, -0.96],
        [0.04, -0.99, -0.85],
        [0.91, 1.04, 0.19]
    ])
    B = np.array([-2.04, -3.73, -1.67])
    
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
