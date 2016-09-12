__author__ = "WonhoShin"

import networkx as nx
import numpy as np
import pandas as pd
import time
import json

def read_graph(network_file=None,network_type='directed'):
    #to cover directed, and undirected graph we use directed graph.
    if network_type=='undirected':
        G = nx.Graph()
    elif network_type=='directed':
        G = nx.DiGraph()
    df = pd.read_csv(network_file,sep="\t", header=None, names=['Node1','Node2','Weight'])
    #Node label should be string not integer even is integer!
    edge_list =[(str(int(row[0])),str(int(row[1])),row[2]) for row in df.values]
    G.add_weighted_edges_from(edge_list)

    return G

def get_sim_matrix_betweenness(fname):
    G = read_graph(network_file=fname, network_type='undirected')

    paths = nx.shortest_path(G)

    f = open(fname + "_similarity_betweenness.txt", "w")
    f.write(json.dumps(paths))
    f.close()

rootdir = "Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1\\"
file_list = [
    "1_ppi_anonym_v2.txt",
    "2_ppi_anonym_v2.txt",
    "3_signal_anonym_directed_v3.txt_duplicates_removed.txt",
    "4_coexpr_anonym_v2.txt",
    "5_cancer_anonym_v2.txt",
    "6_homology_anonym_v2.txt"
]

if __name__ == "__main__":
    for f in file_list:
        print "Process started at " + time.strftime('%H:%M:%S')
        print "File: " + rootdir + f
        get_sim_matrix_betweenness(rootdir + f)
        print "Process terminated at " + time.strftime('%H:%M:%S')

