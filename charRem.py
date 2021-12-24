import sys

old = sys.argv[1]
if len(sys.argv) == 3:
    new = sys.argv[2]
else:
    new = ' '
print(old, new)
f = open('input.txt', "r")
w = open('output.txt', "w")

for line in f:
    newline = line.replace(old, new)
    w.write(newline)
f.close()
w.close()
