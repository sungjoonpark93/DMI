__author__ = 'SungJoonPark'
import networkx as nx
import pandas as pd
from operator import itemgetter

def read_graph(network_file=None,network_type='directed',edge_type='weighted'):
    #to cover directed, and undirected graph we use directed graph.
    if network_type=='undirected':
        G = nx.Graph()
    elif network_type=='directed':
        G = nx.DiGraph()
    df = pd.read_csv(network_file,sep="\t", header=None, names=['Node1','Node2','Weight'])
    #Node label should be string not integer even is integer!
    if edge_type=='weighted':
        edge_list =[(str(int(row[0])),str(int(row[1])),row[2]) for row in df.values]
        G.add_weighted_edges_from(edge_list)
    elif edge_type == 'unweighted':
        edge_list =[(str(int(row[0])),str(int(row[1]))) for row in df.values]
        G.add_edges_from(edge_list)

    return G


def get_high_degree_node(G,top_k=1):
    #return as node, degree tuple list
    node_degree_tuple_sorted_by_degree = sorted(G.degree_iter(),key=itemgetter(1),reverse=True)
    top_k_node_degree_tuple_list = node_degree_tuple_sorted_by_degree[0:top_k]
    return top_k_node_degree_tuple_list



if __name__ =='__main__':
    networkfile = "Q:\DreamChallenge-Disease Module Identification\Tools\COSSY\data\postprocessed/reconstruct/1_ppi/subgraph_587.txt"
    G = read_graph(networkfile,network_type='directed',edge_type='weighted')
    print get_high_degree_node(G, top_k=3)