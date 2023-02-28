f = open("chirag.txt", "w")

lines = ["This is line 1\n", "This is line 2\n", "This is line 3\n"]

f.writelines(lines)

f.close()


f = open("chirag.txt", "r")
fileline = f.readlines()
for line in fileline:
    print(line)
f.close()


with open("chirag.txt", "r") as f:
    print(f.readline())
