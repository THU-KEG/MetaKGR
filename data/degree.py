import json
import re, sys, math, random, csv, types, networkx as nx
from collections import defaultdict

import numpy as np
import pandas as pd
from pandas.core.algorithms import rank


def parse(filename,out):

    reader = pd.read_table(open(filename, 'r'), delimiter='\t',header=None)
    print("Reading and parsing the data into memory...")

    return parse_undirected(reader,out)


def parse_undirected(data,filename):

    G = nx.DiGraph()
    nodes = data[0]
    nodes.append(data[1])
    nodes=set(nodes)
    edges = [(data[0][i], data[1][i]) for i in range(len(data[0]))]
    num_nodes = len(nodes)
    G.add_nodes_from(nodes, rank=rank)
    G.add_edges_from(edges)
    d = nx.degree(G)
    L = len(d)
    S = 0
    nums=[]
    for item in d:
        S+=item[1]
        nums.append(item[1])

    mid=np.median(nums,axis=0)
    mean = L / S
    with open(filename,'w') as f:
        f.write(
            "entity:"+str(num_nodes)+'\n'
            +"relation:"+str(len(set(data[2])))+'\n'
            +"fact:"+str(len(data[0]))+'\n'
            +"degree:"+'{\n'+
                "\tmean:"+str(mean)+'\n'+
                "\tmedian:"+str(mid)+'}'
        )
    return G.degree()
if __name__=='__main__':
    # d=parse("./YAGO11k/raw.kb","./YAGO11k-readme.txt")
    # d = parse("./PQ/raw.kb", "./PQ-readme.txt")
    # d = parse("./nyt10/raw.kb", "./nyt10-readme.txt")
    d = parse("./kinship/raw.kb", "./kinship-readme.txt")


