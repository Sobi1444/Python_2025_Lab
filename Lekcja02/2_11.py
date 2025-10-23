string = "word"
string2 = ""
for char in range(0,len(string)):
    string2 += string[char]
    if char != len(string)-1:
        string2 += "_"
print(string2)

