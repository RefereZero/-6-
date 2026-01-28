N = int(input("Введите количество чисел: "))
sum_numbers = 0

for _ in range(N):
    sum_numbers += int(input("Введите число: "))

print(f"Сумма чисел: {sum_numbers}")
