import math
x, y, z = -15.246, 4.642e-2, 21
s = math.log(y - math.sqrt(abs(x))) * (x - y/2) + math.sin(math.atan(z))**2
print(f"5. s = {s:.3f} (ожидается -182.038)")
