n = int(input("Введите натуральное число n: "))
sum_result = 0

for i in range(1, n + 1):
    sum_result += i * 3

print(f"Сумма: {sum_result}")
