A = int(input("Введите число A: "))
B = int(input("Введите число B (A ≤ B): "))

if A <= B:
    for i in range(A, B + 1):
        print(i, end=" ")
else:
    print("Ошибка: A должно быть ≤ B")
