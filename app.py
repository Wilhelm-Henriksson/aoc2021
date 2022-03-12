#import filereader

f = open("puzzle_input.txt", 'r')
measurements = [int(x) for x in f.readlines()]

counter = 0
first_window = [measurements[0], measurements[1], measurements[2]]
sum_first_window = sum(first_window)

sum_window = 0
for x in range(len(measurements) - 2):
    sum_window = sum(measurements[x:x+3])
    if sum_first_window < sum_window:
        counter = counter + 1
    sum_first_window = sum_window
print(counter)


