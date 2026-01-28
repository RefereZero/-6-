A = int(input("Введите число A (A > B): "))
B = int(input("Введите число B: "))

if A > B:
    start = A if A % 2 != 0 else A - 1
    for i in range(start, B - 1, -2):
        print(i, end=" ")
else:
    print("Ошибка: A должно быть > B")
