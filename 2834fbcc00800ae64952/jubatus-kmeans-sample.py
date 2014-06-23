#!/usr/bin/env python
# coding: utf-8
import sys
import json
import random

import jubatus
from jubatus.common import Datum

host = '127.0.0.1'
port = 9199
name = 'test'

client = jubatus.Clustering(host, port, name)
clusters = [[], []]
for x in xrange(10000):
    if x & 1 == 0:
        # cluster 1
        d = Datum({
            'x' :100 + random.randint(-10, 10),
            'y' : 50 + random.randint(-20, 20)
        })
        clusters[0].append(d)
    else:
        # cluster 2
        d = Datum({
            'x' :-200 + random.randint(-10, 10),
            'y' : 10 + random.randint(-10, 10)
        })
        clusters[1].append(d)

for cluster in clusters:
    client.push(cluster)
    print("{size} data pushed".format(size=len(cluster)))

centers = client.get_k_center()

print("total {size} centers clustered".format(size=len(centers)))
for center in centers:
    print(center.num_values)

data = {'x': -130, 'y': -2}
nearest = client.get_nearest_center(Datum(data))
print("data nearest {d} is {n}".format(d=data, n=nearest.num_values))
