import math
x, y, z = 0.4e4, -0.875, -0.475e-3
s = abs(math.cos(x) - math.cos(y))**(1 + 2*math.sin(y)**2) * (1 + z + z**2/2 + z**3/3 + z**4/4)
print(f"4. s = {s:.5f} (ожидается 1.98727)")
