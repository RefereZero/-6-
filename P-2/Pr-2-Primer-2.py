import math
x, y, z = -4.5, 0.75e-4, -0.845e2
s = ((9 + (x - y)**2) / (x**2 + y**2 + 2))**(1/3) - math.exp(abs(x - y)) * math.tan(z)**3
print(f"2. s = {s:.5f} (ожидается -3.23765)")
