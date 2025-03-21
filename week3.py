a = int(input("입력 진수 결정(16/10/8/2): "))
b = input("값 입력: ")

c = int(b, a)

print("16 진수 =", hex(c))
print("10 진수 =", c)
print("8 진수 =", oct(c))
print("2 진수 =", bin(c))
