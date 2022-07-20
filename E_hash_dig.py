import logging
import sys
from collections import Counter

logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)  # DEBUG, CRITICAL

with open('input_e1.txt', 'r') as f:
    lines = f.readlines()
f.close()
n = 0
a_list = []

for k in range(len(lines)):
    # logging.info(lines[k].strip("\n"))
    workstr = lines[k].strip()
    if k == 0:
        nstr = workstr.strip("\n")
        n = int(nstr)
        logging.info("n = {}".format(n))
    if k == 1:
        astr_list = workstr.strip("\n").split(" ", int(n))
        a_list = list(map(int, astr_list))
        logging.info("a_list = {}".format(a_list))

voc = Counter(a_list)

setOfElems = set()
is_double = False
for k, v in voc.items():
    # print(k, v)
    if v in setOfElems:
        is_double = True
        break
    else:
        setOfElems.add(v)
if is_double:
    print("NO")
else:
    print("YES")