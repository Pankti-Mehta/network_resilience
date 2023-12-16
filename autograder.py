# Firstname Lastname
# NetID
# COMP 182 Spring 2021 - Homework 4, Problem 3

# You may NOT import anything apart from already imported libraries.
# You can use helper functions from comp182.py and provided.py, but they have
# to be copied over here.

from collections import *

def compute_largest_cc_size(g: dict) -> int:
    max_size = 1
    h = {}
    for vert in g.keys():
        h[vert] = False
    size_tracker = 1
    for vert1 in g.keys():
        if h[vert1] == False:
            h[vert1] = True
            vert_storer = deque()
            vert_storer.append(vert1)
            while len(vert_storer) > 0:
                vert = vert_storer.popleft()
                for nbr in g[vert]:
                    if h[nbr] == False:
                        h[nbr] = True
                        vert_storer.append(nbr)
                        size_tracker = size_tracker + 1
            if size_tracker > max_size:
                max_size = size_tracker
            size_tracker = 1
    return max_size
    #return 0
# print(compute_largest_cc_size({
#     1:[2,3],
#     2:[16,17],
#     3:[4,5],
#     4:[],
#     5:[],
#     6:[7],
#     7:[8],
#     8:[],
#     9:[],
#     10:[11,15],
#     11:[14,13],
#     12:[],
#     13:[],
#     14:[],
#     15:[],
#     16:[],
#     17:[]
# }
# ))