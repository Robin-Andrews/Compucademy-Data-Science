"""
Gambler's Fallacy with Python
"""

import itertools
import random
from collections import Counter

NUM_COINS = 4
NUM_FLIPS = 1000


def new_sequence(event_counter):
    seq = ""
    for i in range(NUM_COINS):
        seq += coin_flip()
    event_counter[seq] += 1


def coin_flip():
    return "T" if random.random() < 0.5 else "H"


perms = ["".join(x) for x in list(itertools.product("TH", repeat=NUM_COINS))]
event_counter = {key: 0 for key in perms}
for i in range(NUM_FLIPS):
    new_sequence(event_counter)


for k, v in event_counter.items():
    proportion = str(round(v / NUM_FLIPS * 100, 2)) + "%"
    print(k, proportion)
