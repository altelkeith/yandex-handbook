a = float(input())
b = float(input())
c = float(input())
if a == b == c == 0:
    print("Infinite solutions")
elif a == c == 0:
    print("0.00")
elif a == b == 0:
    print("No solution")
elif a == 0 and b != 0 and c != 0:
    x = (c / b) * (-1)
    print(float('{:.2f}'.format(x)))
else:
    d = (b ** 2) - 4 * a * c
    x_one = ((-1 * b) + d ** (0.5)) / (2 * a)
    if d == 0:
        print(float('{:.2f}'.format(x_one)))
    elif d > 0:
        x_two = ((-1 * b) - d ** (0.5)) / (2 * a)
        print(float('{:.2f}'.format(min(x_one, x_two))), float('{:.2f}'.format(max(x_one, x_two))))
    else:
        print("No solution")