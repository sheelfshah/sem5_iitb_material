s = poly(0, 's')
G1 = s * s + (1 / s)
C1 = G / (1 + G)
G2 = C1 * (1 / s)
C2 = G2 / (1 + s * G2)
disp(C2)
