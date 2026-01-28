num = input("Введите число: ")

even_digits = []
odd_digits = []

if len(num) > 0 and num[0].isdigit():
    if int(num[0]) % 2 == 0:
        even_digits.append(num[0])
    else:
        odd_digits.append(num[0])

if len(num) > 1 and num[1].isdigit():
    if int(num[1]) % 2 == 0:
        even_digits.append(num[1])
    else:
        odd_digits.append(num[1])

if len(num) > 2 and num[2].isdigit():
    if int(num[2]) % 2 == 0:
        even_digits.append(num[2])
    else:
        odd_digits.append(num[2])

print(f"Четные цифры: {even_digits}")
print(f"Нечетные цифры: {odd_digits}")
