with open("puzzle_input.txt") as f:
    values = [i for i in f.read().strip().split("\n")]

gamma_rate = ""
epsilon_rate = ""

for y in range(0, len(values[0])):
    zeros = 0
    ones = 0
    for x in values: 
        if x[y] == '0': 
            zeros += 1
        else: 
            ones += 1
    if ones > zeros: 
        gamma_rate += '1'
        epsilon_rate += '0'
    else: 
        gamma_rate += '0'
        epsilon_rate += '1'

g = int(gamma_rate, 2)
e = int(epsilon_rate, 2)

pwr = g * e 
#print("gamma is ", g, "epsilon is ", e)
#print("power is ", pwr)

# part 2

oxygen = values
co2 = values
col = 0

while len(oxygen) > 1:
    zeros = 0
    ones = 0
    
    for row in oxygen: 
        if row[col] == '0': 
            zeros += 1
        else: 
            ones += 1
    if zeros > ones: 
        oxygen = [row for row in oxygen if row[col] == '0']
    else: 
        oxygen = [row for row in oxygen if row[col] == '1']

    col += 1

col = 0
while len(co2) > 1:
    zeros = 0
    ones = 0
    
    for row in co2: 
        if row[col] == '0': 
            zeros += 1
        else: 
            ones += 1
    if zeros > ones: 
        co2 = [row for row in co2 if row[col] == '1']
    else: 
        co2 = [row for row in co2 if row[col] == '0']

    col += 1

print("O2 rate is ", oxygen)
print("CO2 rate is ", co2)

o2 = int(''.join(oxygen), 2)
co2 = int(''.join(co2), 2)
life = o2 * co2
print("Life support rating is ", life)