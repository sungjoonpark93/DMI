__author__ = 'SungJoonPark'

import networkx as nx
import pandas as pd
import network_base

def is_star_graph(networkfile):

    pass



if __name__ =='__main__':
    subgraphfile = "Q:\DreamChallenge-Disease Module Identification\Tools\COSSY\data\postprocessed/reconstruct/1_ppi/subgraph_587.txt"
    G=network_base.read_graph(subgraphfile,network_type='directed',edge_type='weighted')
    print G.number_of_nodes()
    print network_base.get_high_degree_node(G,top_k=300)

