import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)  # DEBUG, CRITICAL

with open('input_d2.txt', 'r') as f:
    lines = f.readlines()
f.close()

for k in range(len(lines)):
    # logging.info(lines[k].strip("\n"))
    workstr = lines[k].strip()
    if k == 0:
        nm = workstr.strip("\n").split(" ", 2)
        word1 = nm[0]
        word2 = nm[1]
        logging.info("word1  = {}, word2  = {}".format(word1, word2))

voc = {}
# print(ord('A'),ord('a'))
for i in range(65, 65+26):
    # print(chr(i))
    voc.update({i:0})
for i in range(97, 97+26):
    # print(chr(i))
    voc.update({i:0})

for ch in word2:
    tmp = voc.get(ord(ch))
    tmp += 1
    voc.update({ord(ch): tmp})

res = 0
for ch in word1:
    res += voc.get(ord(ch))
print(res)