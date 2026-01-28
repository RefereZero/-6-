A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A < B:
    for i in range(A, B + 1):
        print(i, end=" ")
else:
    for i in range(A, B - 1, -1):
        print(i, end=" ")
