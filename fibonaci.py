n = int(input("Masukan angka : "))
a, b = 0, 1
for i in range(n):
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b