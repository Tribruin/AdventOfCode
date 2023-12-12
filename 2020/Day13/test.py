from sympy.ntheory.modular import crt

with open("Day13/Day13-Input.txt") as fin:
    data = fin.read().split("\n")

modulos = []
remainders = []

busTimestamps = data[1].split(",")
for i in range(len(busTimestamps)):
    if busTimestamps[i].isnumeric():
        modulos.append(int(busTimestamps[i]))
        remainders.append((-i) % modulos[-1])

print(modulos)
print(remainders)

ans = crt(modulos, remainders)

print(ans)
