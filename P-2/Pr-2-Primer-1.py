import math
x, y, z = 14.26, -1.22, 3.5e-4
s = (2 * math.cos(x - 2/3)) / (1/2 + math.sin(y)**2) * (1 + z**2 / (3 - z**2 / 5))
print(f"s = {s:.6f}")
print(f"Ожидаемый ответ: 0.749155")
