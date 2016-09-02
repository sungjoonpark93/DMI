__author__ = 'SungJoonPark'

import pandas as pd
import base
import networkx as nx
import operator

def assign_one_node_to_cluster(node, genesetfile , genesetfile_format='gmt', networkfile=None ,outputfile=None,output_format='gmt'):
    G = nx.DiGraph()
    df = pd.read_csv(networkfile,sep="\t", header=None, names=['Node1','Node2','Weight'])
    edge_list =[(str(int(row[0])),str(int(row[1]))) for row in df.values]
    G.add_edges_from(edge_list)

    geneset_list = base.read_genesetfile(genesetfile=genesetfile , input_format=genesetfile_format)

    count_dict={}
    for i,geneset in enumerate(geneset_list):
        if len(geneset)<100:
            count = 0
            for gene in geneset:
                if (G.has_edge(gene,node)) or (G.has_edge(node,gene)):
                    count = count +1


            count_dict[i] = count

    count_tuple_list = sorted(count_dict.items(), key=operator.itemgetter(1) ,reverse=True)
    top_connected_cluster = count_tuple_list[0][0]


    geneset_list[top_connected_cluster] = geneset_list[top_connected_cluster] + [node]

    base.write_genesetfile(geneset_list,outputfile=outputfile,output_format=output_format)

if __name__ =='__main__':
    node = "6934"
    genesetfile = "Q:\DreamChallenge-Disease Module Identification\Tools\COSSY\data/1_ppi_6934_removed_network.gmt"
    networkfile = "Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1/1_ppi_anonym_v2.txt"
    assign_one_node_to_cluster(node, genesetfile, networkfile=networkfile, outputfile="Q:\DreamChallenge-Disease Module Identification\Tools\COSSY\data/1_ppi_6934_removed_network_6934_reassigned.gmt",output_format='gmt')
