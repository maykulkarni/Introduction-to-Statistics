from __future__ import division

import math

data3 = [1, 2, 3, 4, 5, 6]


def mean(data):
    return sum(data) / len(data)


def median(data):
    mid = int(len(data) / 2)
    return sorted(data)[mid]


def mode(data):
    counts = dict()
    for numbers in data:
        if numbers in counts:
            count = counts[numbers]
            counts[numbers] = count + 1
        else:
            counts[numbers] = 1
    return sorted(counts, key=counts.get, reverse=True)[0]


def variance(data):
    mean_ = mean(data)
    normalised_list = [(x - mean_) for x in data]
    squared_list = [x ** 2 for x in normalised_list]
    return sum(squared_list) / len(data)


def likelihood(dist, data):
    ans = 1
    for c in data:
        ans *= dist[c]
    return ans


def running_mean(oldmean, n, x):
    sum_of_x = oldmean * n
    new_mean = (sum_of_x + x) / (n + 1)
    return new_mean


def std_dev(data):
    return math.sqrt(variance(data))


print likelihood({'A': 0.2, 'B': 0.2, 'C': 0.2, 'D': 0.2, 'E': 0.2}, 'ABCEDDECAB')
