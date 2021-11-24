s = poly(0, 's')

T = [1, 2, 3;
    3, 4, 5;
    4, 6, 9]
A = [1, 5, 7;
    2, 0, 4;
    3, 3, 2]
B = [2;
    5;
    7]
C = [3, 1, 4]
D = 34

T_ = inv(T)
A_ = T_ * A * T
B_ = T_ * B
C_ = C * T

// part A
G = D + C * inv(s * eye(3, 3) - A) * B
G_ = D + C_ * inv(s * eye(3, 3) - A_) * B_
disp(G)
disp(G_)

// part B
disp(spec(A))
disp(roots(G.den))

// part C
G1 = (3 + 4*s + s^2) / (1 + s + s^2)
G2 = (3 + 2*s) / (1 + s + s^2)
ssr1 = tf2ss(G1)
ssr2 = tf2ss(G2)
disp(ssr1)
disp(ssr2)
// D is non-zero for the proper G(s), and 0 for the strictly proper one
