import logging
import sys
import math

logging.basicConfig(stream=sys.stderr, level=logging.CRITICAL)  # DEBUG, CRITICAL

with open('input_a1.txt', 'r') as f:
    lines = f.readlines()
f.close()
n = 0
a_list = []
e = 0
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
    if k == 2:
        estr = workstr.strip("\n")
        e = int(estr)
        logging.info("e = {}".format(e))
L = 0
R = n - 1
sig = ''
while L <= R:
    m = math.floor((L+R) / 2)
    if a_list[m] < e:
        L = m + 1
        # print('>', m)
        sig = '+'
    elif a_list[m] > e:
        R = m - 1
        # print('<', m)
        sig = '-'
    else:
        print(m)
        exit(0)

if e < a_list[0]:
    print(0)
    exit(0)
elif e > a_list[n - 1]:
    print(n)
    exit(0)
else:
    if sig == '+':
        print(m+1)
    else:
        print(m)


