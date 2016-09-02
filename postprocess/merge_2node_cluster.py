__author__ = 'WonhoShin'

import numpy as np
import pandas as pd
import networkx as nx
import argparse

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


def read_genesetfile(genesetfile=None,input_format="txt"):
    geneset_list = []
    with open(genesetfile,'r') as r:
        for line in r:
            if input_format =='txt':
                #Node label should be string not integer even is integer!
                geneset_list.append(line.strip().split("\t"))
            elif input_format =='gmt':
                #Node label should be string not integer even is integer!
                geneset_list.append(line.strip().split("\t")[2:])
    geneset_list = [gene_list for gene_list in geneset_list]
    return geneset_list

def separate_geneset_2node_or_not(geneset_list):
    geneset_2node = [x for x in geneset_list if len(x) == 2]
    geneset_gt3 = [x for x in geneset_list if len(x) > 2]
    return geneset_2node, geneset_gt3

def merge_2node_cluster(geneset_2node, geneset_gt3):
    _geneset = []
    sep_geneset = []
    for gpair in geneset_2node:
        _geneset.extend(gpair)
    if len(_geneset) <= 2:
        return geneset_gt3

    k = len(_geneset)/100
    if len(_geneset)%100:
        k += 1
    cluster_size = len(_geneset) / k
    sep_boundary = [x *( cluster_size) for x in range(k)]
    sep_boundary.append(len(_geneset))

    for i in range(len(sep_boundary) - 1):
        sep_geneset.append(_geneset[sep_boundary[i]:sep_boundary[i+1]])


    geneset = geneset_gt3
    if len(sep_geneset) > 0:
        geneset.extend(sep_geneset)
    return geneset

def export_merged_geneset(geneset, network_name, geneset_file):
    f = open(geneset_file + '_2node_removed.gmt', 'w')
    for i, glist in enumerate(geneset):
        f.write(str(i+1) + '\t' + network_name + '\t' + '\t'.join(glist) + '\n')
    f.close()

def run(network_file, network_name, geneset_file, geneset_fmt):
    G = read_graph(network_file, network_type="undirected")
    geneset_list = read_genesetfile(geneset_file,input_format=geneset_fmt)
    geneset_2node, geneset_gt3 = separate_geneset_2node_or_not(geneset_list)
    geneset_merged = merge_2node_cluster(geneset_2node, geneset_gt3)
    export_merged_geneset(geneset_merged, network_name, geneset_file)



if __name__ =='__main__':
    network_list = []
    network_list.append(['1_ppi_anonym_aligned_v2', 'Q:\DreamChallenge-Disease Module Identification\Tools\SPICi\SPICi\output\subchallenge2\conf_avg_10_0.5.txt'])
    # network_list.append(['1_ppi_anonym_v2', '1_ppi_6934_removed_network_6934_reassigned'])
    # network_list.append(['2_ppi_anonym_v2', '2_ppi_anonym_v2'])
    # network_list.append(['3_signal_anonym_directed_v3', '3_signal_anonym_directed_v3'])
    # network_list.append(['4_coexpr_anonym_v2', '4_coexpr_anonym_v2'])
    # network_list.append(['5_cancer_anonym_v2', '5_cancer_anonym_v2'])
    # network_list.append(['6_homology_anonym_v2', '6_homology_anonym_v2'])
    for network_name, geneset_name in network_list:
        network_file = "Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge2/" + network_name + ".txt"
        #geneset_file = "Q:/DreamChallenge-Disease Module Identification/Tools/COSSY/data/" + geneset_name + ".gmt"
        geneset_file = geneset_name
        G=read_graph(network_file,network_type='undirected')
        geneset_list = read_genesetfile(geneset_file,input_format='txt')
        geneset_2node, geneset_gt3 = separate_geneset_2node_or_not(geneset_list)
        #get_freq(geneset_2node, geneset_gt3, G)
        geneset_merged = merge_2node_cluster(geneset_2node, geneset_gt3)
        export_merged_geneset(geneset_merged, geneset_name)