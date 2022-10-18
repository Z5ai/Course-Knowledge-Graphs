import sys

filename = sys.argv[1]
file = open(filename, "r")
n = int(file.readline())

degrees = n * [0]

for line in file:
    a, b = line.split(' ')
    a = int(a)
    degrees[a] += 1




result = []
max_degree = 0

for i in range(n):
    if degrees[i] > max_degree:
        max_degree = degrees[i]
        result = [i]
    elif degrees[i] == max_degree:
        result.append(i)

print(result)