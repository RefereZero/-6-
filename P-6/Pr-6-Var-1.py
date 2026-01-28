N = int(input("Введите количество элементов массива N: "))

if N <= 0:
    print("Количество элементов должно быть положительным числом")
else:
    arr = []
    print("Введите элементы массива:")
    for i in range(N):
        element = int(input(f"Элемент {i + 1}: "))
        arr.append(element)

    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element

    print("\nИсходный массив:", arr)
    print(f"Максимальный элемент: {max_element}")

    print("Массив в обратном порядке:", end=" ")
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=" ")
    print()
