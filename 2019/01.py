import math

with open("01.txt", "r") as f:
    inp = f.read()
modules = [int(x) for x in inp.split()]
fuel = [math.floor(int(x) / 3) - 2 for x in modules]
print(sum(fuel))


fuel_sum2 = 0

for m in modules:
    required = math.floor(m / 3) - 2
    if required > 0:
        fuel_sum2 += required
        modules.append(required)
print(fuel_sum2)
