### Part 1: find the first winning board (complete row or col). Find sum of all unmarked numbers from that board, then * last drawn num
f = open('puzzle_input.txt', 'r')
pool = [int(x) for x in f.readline().split(",")]
lines = []
for i, line in enumerate(f): 
    if i >= 1 and line: 
        lines.append(line.split())

not_drawn: set[int]
boards = list(filter(None, lines))


for row in range(len(boards)):
    for col in range(len(boards[row])): 
            int(boards[row][col])

for d in pool:
    for row in range(len(boards)):
        for board in range(len(boards[row])): 
            not_drawn.discard(d)

def winner():
    pass

