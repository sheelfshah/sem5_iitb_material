s = poly(0, 's')

g = (s + 100) * (s + 100) / ((s + 4)^3)
G = syslin("c", g)

// evans(G, 1000)
nyquist(1000 * G)
