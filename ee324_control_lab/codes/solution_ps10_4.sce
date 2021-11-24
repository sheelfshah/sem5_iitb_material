s = poly(0, 's')

A = [0, -10, 0;
    0, 0, -1;
    -4, 0, 0]
B = [0;
    0;
    -5]
C = [1, 0, 0]

G1 = C * inv(s * eye(3, 3) - A) * B
disp(G1)
disp(simp(G1))
disp(roots(G1.den))
disp(B, A*B, A*A*B)
