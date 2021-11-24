s = poly(0, 's')

g =  s^5 + 3*s^4 + 5*s^3 + 4*s^2 + s + 3
disp(routh_t(g), "Part A")

g = s^5 + 6*s^3 + 5*s^2 + 8*s + 20
disp(routh_t(g), "Part B")

g = s^5 - 2*s^4 + 3*s^3- 6*s^2 + 2*s - 4
disp(routh_t(g), "Part C")

g = s^6 + s^5 - 6*s^4 + s^2 + s - 6
disp(routh_t(g), "Part D")
