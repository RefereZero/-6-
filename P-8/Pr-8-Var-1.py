def main():
    N = int(input("Введите размер квадратной матрицы N: "))

    if N <= 0:
        print("Размер матрицы должен быть положительным числом")
        return

    A = []
    print(f"\nВведите элементы матрицы {N}xN:")

    for i in range(N):
        row = []
        for j in range(N):
            element = float(input(f"A[{i + 1},{j + 1}] = "))
            row.append(element)
        A.append(row)

    print("\nИсходная матрица:")
    for i in range(N):
        for j in range(N):
            print(f"{A[i][j]:8.2f}", end=" ")
        print()

    sum_positive = 0
    count_positive = 0
    elements = []

    for i in range(N):
        for j in range(N):
            if j > i and A[i][j] > 0:  # j > i - элементы над главной диагональю
                sum_positive += A[i][j]
                count_positive += 1
                elements.append(A[i][j])

    print(f"\nЭлементы над главной диагональю: {elements}")
    print(f"Сумма положительных элементов над главной диагональю: {sum_positive:.2f}")
    print(f"Количество положительных элементов над главной диагональю: {count_positive}")


if __name__ == "__main__":
    main()
