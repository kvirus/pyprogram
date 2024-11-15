import numpy as np
import itertools

def find_closese_sum(numbers, targets):
    numbers = numbers[:]
    for t in targets:
        if not numbers:
            break
        combs = sum([list(itertools.combinations(numbers, r))
                           for r in range(1, len(numbers)+1)], [])
        sums = np.asarray(list(map(sum, combs)))
        bestcomb = combs[np.argmin(np.abs(np.asarray(sums) - t))]
        numbers = list(set(numbers).difference(bestcomb))
        print("Target: {},  combination: {}".format(t, bestcomb))

targets = [14,16,17]
numbers = [5,2,5,2,2,5,2,5,16]
find_closese_sum(numbers, targets)