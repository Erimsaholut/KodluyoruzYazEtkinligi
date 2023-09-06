from sympy import symbols, Eq, solve

X, Y, Z, A = symbols('X Y Z A')

denklem1 = Eq(10 * X, 30)
denklem2 = Eq(15 * Y, 30)
denklem3 = Eq(30 * Z, 30)
denklem4 = Eq(A * X + A * Y - A * Z, 30)

cozum = solve((denklem1, denklem2, denklem3, denklem4), A)

cozum_A_degeri = cozum[A].subs({X: 3, Y: 2, Z: 1})
print("A'nın değeri:", cozum_A_degeri)