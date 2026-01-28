num = int(input("Введите целое число больше 1: "))

if num <= 1:
    print("Число должно быть больше 1")
elif num == 2 or num == 3:
    print(f"{num} - простое число")
elif num % 2 == 0 or num % 3 == 0:
    print(f"{num} - составное число")
else:
    is_prime = True

    if num % 5 == 0 or num % 7 == 0 or num % 11 == 0 or num % 13 == 0:
        is_prime = False

    if is_prime:
        print(f"{num} - простое число")
    else:
        print(f"{num} - составное число")
