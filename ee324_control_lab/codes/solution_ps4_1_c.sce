s = poly(0, 's')
G1 = 3 * s * (s / (1 + s))
G2 = 1 / (1 + s)
C2 = G2 / (1 + G2)
// x = r - c

// y = 2sx - 4c
// y = 2sr - c(2s+4)

// c = (G1x + y).C2
// c = (G1r - G1c + 2sr - c(2s+4)).C2
// c = G1C2r + 2sC2r - c(G1 + 2s +4)C2
C = (G1 * C2 + 2 * s * C2) / (1 + C2*(G1 + 2*s + 4))
disp(C)
