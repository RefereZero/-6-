import math


def main():
    print("=== Программа для вычисления площади геометрических фигур ===")
    print("Выберите фигуру:")
    print("1. Квадрат")
    print("2. Прямоугольник")
    print("3. Треугольник")
    print("4. Круг")
    print("5. Параллелограмм")
    print("6. Трапеция")
    print("7. Ромб")
    print("8. Эллипс")

    try:
        choice = int(input("Введите номер фигуры (1-8): "))

        if choice == 1:
            side = float(input("Введите длину стороны квадрата: "))
            if side > 0:
                area = side * side
                print(f"Площадь квадрата: {area:.2f}")
            else:
                print("Длина стороны должна быть положительной")

        elif choice == 2:
            length = float(input("Введите длину прямоугольника: "))
            width = float(input("Введите ширину прямоугольника: "))
            if length > 0 and width > 0:
                area = length * width
                print(f"Площадь прямоугольника: {area:.2f}")
            else:
                print("Длина и ширина должны быть положительными")

        elif choice == 3:
            print("Выберите способ вычисления:")
            print("1. По основанию и высоте")
            print("2. По трем сторонам (формула Герона)")
            method = int(input("Введите способ (1 или 2): "))

            if method == 1:
                base = float(input("Введите длину основания: "))
                height = float(input("Введите высоту: "))
                if base > 0 and height > 0:
                    area = 0.5 * base * height
                    print(f"Площадь треугольника: {area:.2f}")
                else:
                    print("Основание и высота должны быть положительными")

            elif method == 2:
                a = float(input("Введите длину первой стороны: "))
                b = float(input("Введите длину второй стороны: "))
                c = float(input("Введите длину третьей стороны: "))
                if a > 0 and b > 0 and c > 0:
                    if a + b > c and a + c > b and b + c > a:
                        p = (a + b + c) / 2
                        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
                        print(f"Площадь треугольника: {area:.2f}")
                    else:
                        print("Треугольник с такими сторонами не существует")
                else:
                    print("Длины сторон должны быть положительными")
            else:
                print("Неверный выбор метода")

        elif choice == 4:
            radius = float(input("Введите радиус круга: "))
            if radius > 0:
                area = math.pi * radius * radius
                print(f"Площадь круга: {area:.2f}")
            else:
                print("Радиус должен быть положительным")

        elif choice == 5:
            base = float(input("Введите длину основания: "))
            height = float(input("Введите высоту: "))
            if base > 0 and height > 0:
                area = base * height
                print(f"Площадь параллелограмма: {area:.2f}")
            else:
                print("Основание и высота должны быть положительными")

        elif choice == 6:
            a = float(input("Введите длину первого основания: "))
            b = float(input("Введите длину второго основания: "))
            height = float(input("Введите высоту: "))
            if a > 0 and b > 0 and height > 0:
                area = 0.5 * (a + b) * height
                print(f"Площадь трапеции: {area:.2f}")
            else:
                print("Основания и высота должны быть положительными")

        elif choice == 7:
            print("Выберите способ вычисления:")
            print("1. По диагоналям")
            print("2. По стороне и высоте")
            method = int(input("Введите способ (1 или 2): "))

            if method == 1:
                d1 = float(input("Введите длину первой диагонали: "))
                d2 = float(input("Введите длину второй диагонали: "))
                if d1 > 0 and d2 > 0:
                    area = 0.5 * d1 * d2
                    print(f"Площадь ромба: {area:.2f}")
                else:
                    print("Диагонали должны быть положительными")

            elif method == 2:
                side = float(input("Введите длину стороны: "))
                height = float(input("Введите высоту: "))
                if side > 0 and height > 0:
                    area = side * height
                    print(f"Площадь ромба: {area:.2f}")
                else:
                    print("Сторона и высота должны быть положительными")
            else:
                print("Неверный выбор метода")

        elif choice == 8:
            a = float(input("Введите длину большой полуоси: "))
            b = float(input("Введите длину малой полуоси: "))
            if a > 0 and b > 0:
                area = math.pi * a * b
                print(f"Площадь эллипса: {area:.2f}")
            else:
                print("Полуоси должны быть положительными")

        else:
            print("Неверный выбор фигуры. Пожалуйста, выберите номер от 1 до 8.")

    except ValueError:
        print("Ошибка: пожалуйста, вводите числовые значения")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
