def read_matrix_from_file_simple(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        lines = [line.strip() for line in lines if line.strip()]

        if not lines:
            return None

        A = []
        for line in lines:
            elements = line.split()
            try:
                row = [float(elem) for elem in elements]
                A.append(row)
            except ValueError:
                print(f"Ошибка: строка содержит некорректные данные: {line}")
                return None

        N = len(A)
        for row in A:
            if len(row) != N:
                print(f"Ошибка: матрица не квадратная")
                return None

        return A

    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return None


def main_simple():
    input_filename = "AAA_ZIV-25_vvod.txt"
    output_filename = "AAA_ZIV-25_vivod.txt"

    print(f"Чтение матрицы из файла: {input_filename}")

    A = read_matrix_from_file_simple(input_filename)

    if A is None:
        print("Не удалось прочитать матрицу из файла")
        return

    N = len(A)
    print(f"Размер матрицы: {N}x{N}")

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
            if j > i and A[i][j] > 0:
                sum_positive += A[i][j]
                count_positive += 1
                elements.append(A[i][j])

    print(f"\nЭлементы над главной диагональю: {elements}")
    print(f"Сумма положительных элементов: {sum_positive:.2f}")
    print(f"Количество положительных элементов: {count_positive}")

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write("Исходная матрица:\n")
        for i in range(N):
            for j in range(N):
                f.write(f"{A[i][j]:8.2f} ")
            f.write("\n")

        f.write(f"\nПоложительные элементы над диагональю: {elements}\n")
        f.write(f"Их сумма: {sum_positive:.2f}\n")
        f.write(f"Их количество: {count_positive}\n")

    print(f"\nРезультаты сохранены в файл: {output_filename}")


if __name__ == "__main__":
    main_simple()