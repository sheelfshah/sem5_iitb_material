s = poly(0, 's')
G = (1 / s^2) * (50 * s / (s^2 + s + 100)) * (s - 2)
C = G / (1 + G)
disp(C)
