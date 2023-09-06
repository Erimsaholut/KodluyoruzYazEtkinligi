from sympy import symbols, Eq, solve

T, K = symbols('T K')
toplam_bas = 36
toplam_bacak = 100
denklem1 = Eq(T + K, toplam_bas)
denklem2 = Eq(2 * T + 4 * K,toplam_bacak)

cozum = solve((denklem1, denklem2), (T, K))

print("Tavuk sayısı:", cozum[T])
print("Koyun sayısı:", cozum[K])