import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)  # DEBUG, CRITICAL
with open('input_f1.txt', 'r') as f:
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