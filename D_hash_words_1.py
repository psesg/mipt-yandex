import array as arr

with open('input_d2.txt', 'r') as f:
    line = f.readline()
f.close()

nm = line.strip("\n").split(" ", 2)
word1 = nm[0]
word2 = nm[1]

lst = [0]*52
ar = arr.array('l', lst)

for ch in word2:
    t = ord(ch)
    if t >= 97:
        ar[t - 97 + 26] += 1
    else:
        ar[t - 65] += 1

res = 0
for ch in word1:
    t = ord(ch)
    if t >= 97:
        res += ar[t - 97 + 26]
    else:
        res += ar[t - 65]
print(res)
