

from collections import deque
from comp182 import *
from provided import *
from autograder import *
import random


"""
Plot data in the dictionary d on the current plot as bars.


Arguments:
d     -- dictionary
xmin  -- optional minimum value for x axis
label -- optional legend label


Returns:
None
"""
def compute_largest_cc_size(g: dict) -> int:
   max_size = 0
   h = {}
   for vert in g.keys():
       h[vert] = False
   for vert1 in g.keys():
       if h[vert1] == False:
           h[vert1] = True
           vert_storer = deque()
           vert_storer.append(vert1)
           size_tracker = 0
           while len(vert_storer) > 0:
               vert = vert_storer.pop()
               for nbr in g[vert]:
                   if h[nbr] == False:
                       h[nbr] = True
                       vert_storer.append(nbr)
                       size_tracker = size_tracker + 1
           if size_tracker > max_size:
               max_size = size_tracker
   return max_size
def prob(g):
   return (total_degree(g)/2) / (len(g) * (len(g) - 1) / 2)




# Firstname Lastname
# NetID
# COMP 182 Spring 2021 - Homework 4, Problem 3


# You can import any standard library, as well as Numpy and Matplotlib.
# You can use helper functions from comp182.py, provided.py, and autograder.py,
# but they have to be copied over here.


# Your code here...




graph1 = read_graph("rf7.repr")
graph2 = erdos_renyi(len(graph1), prob(graph1))
graph3 = upa(len(graph1), int((total_degree(graph1)/2)/1239))


#avg edges make func(graph1)


# print(graph1, graph2, graph3)


def random_attack(g):
   h = copy_graph(g)
   num_cc = {}
   for x in range(0, int(.2*len(g))):
       node_to_pop = random.choice(list(h.keys()))
       for g_val in h[node_to_pop]:
           h[g_val].remove(node_to_pop)
       h.pop(node_to_pop)
       num_cc[x] = compute_largest_cc_size(h)
   return num_cc


#test cases make up
def targeted_attack(g):
   cpy = copy_graph(g)
   num_cc = {}
   ndsDeg = {}
   #create a dictionary with node, and its value as the degree
   for ke in list(cpy.keys()):
       ndsDeg[ke] = len(cpy[ke])#the number of stuff in the values for that ke


   #go over ndsDeg and pop nodes + values that are the max
   for nd in range(0, int(.2*len(g))):
       node_to_pop = random.choice(list(cpy.keys()))
       count = 0
       for key, value in ndsDeg.items():
           if value > count:
               count = value
               node_to_pop = key
       for g_val in cpy[node_to_pop]:
           cpy[g_val].remove(node_to_pop)
       cpy.pop(node_to_pop)
       ndsDeg.pop(node_to_pop)
       num_cc[nd] = compute_largest_cc_size(cpy)
   return num_cc






plot_lines([random_attack(graph1), random_attack(graph2), random_attack(graph3), targeted_attack(graph1), targeted_attack(graph2), targeted_attack(graph3)], "Graph", "number of nodes removed", "size of the largest connected component", ["Random Attack: Graph 1","Random Attack: Graph 2","Random Attack: Graph 3", "Targeted Attack: Graph 1", "Targeted Attack: Graph 2","Targeted Attack: Graph 3"], filename=None)

