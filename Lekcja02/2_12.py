line = "Abcd Efgh Ijkl"
first = "".join(word[0] for word in line.split())
print(first)
last = "".join(word[len(line.split())] for word in line.split())
print(last)