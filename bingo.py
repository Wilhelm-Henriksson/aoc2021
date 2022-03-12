f = open('puzzle_input.txt', 'r')
pool = [int(x) for x in f.readline().split(",")]
#draws = [pool[i:i+5] for i in range(0, len(pool), 5)]
lines = []
for i, line in enumerate(f): 
    if i >= 1: 
        lines.append(line.strip())

lines = list(filter(None, lines))
boards = [lines[i:i+5] for i in range(0, len(lines), 5)]

for i in range(len(boards)): 
    for j in range(len(boards[i])):
        pass
#while no_winner: 
   # pass
print(boards[0][3])

def no_winner():
    pass

