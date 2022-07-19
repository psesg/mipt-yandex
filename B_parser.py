import logging
import sys
from collections import deque

logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)  # DEBUG, CRITICAL

with open('input_b1.txt', 'r') as f:
    lines = f.readlines()
strS =''
for k in range(len(lines)):
    # logging.info(lines[k].strip("\n"))
    workstr = lines[k].strip()
    if k == 0:
        strS = workstr.strip("\n")
        logging.info("strS = {}".format(strS))
st_1 = deque()
st_2 = deque()
st_3 = deque()
chpop = ''
try:
    for ch in strS:
        if ch == '{':
            st_1.append(ch)
        if ch == '[':
            st_2.append(ch)
        if ch == '(':
            st_3.append(ch)
        if ch == '}':
            chpop = st_1.pop()
        if ch == ']':
            chpop = st_2.pop()
        if ch == ')':
            chpop = st_3.pop()
except Exception as e:
    print("no")
else:
    if len(st_1) == 0 and len(st_2) == 0 and len(st_3) == 0:
        print("yes")
    else:
        print("no")

