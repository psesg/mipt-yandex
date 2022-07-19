import logging
import sys
import math

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)  # DEBUG, CRITICAL

with open('input_d1.txt', 'r') as f:
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
