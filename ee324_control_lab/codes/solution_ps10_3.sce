s = poly(0, 's')

A = [1, 0, 0;
    0, 2, 0;
    0, 0, 3]
B = [2;
    5;
    7]
B_ = [0;
    5;
    7]
C = [3, 1, 4]
C_ = [3, 0, 4]

G1 = C * inv(s * eye(3, 3) - A) * B
G2 = C * inv(s * eye(3, 3) - A) * B_
G3 = C_ * inv(s * eye(3, 3) - A) * B
disp(roots(G1.den))
disp(roots(G2.den))
disp(roots(G3.den))
