s = poly(0, 's')
G1 = (s + 3) / (4 + 5*s + s^2)
G2 = (s + 1) / (4 + 5*s + s^2)
ssr1 = tf2ss(G1)
ssr2 = tf2ss(G2)
disp(ssr1)
disp(ssr2)