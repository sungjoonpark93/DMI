__author__ = 'WonhoShin'

import numpy as np
import pandas as pd
import networkx as nx

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

def get_freq(geneset_2node, geneset_gt3, G):
    tp = [[],[],[],[]]
    tjfak = []
    for gpair in geneset_2node:
        g1, g2 = gpair[0], gpair[1]
        print g1, g2
        print G.neighbors(g1)
        print G.neighbors(g2)
        if len(G.neighbors(g1)) == 1 and len(G.neighbors(g2)) == 1:
            tp[0].append(gpair)
            continue
        min_len = 0x7fffffff
        for t in geneset_2node:
            if g1==t[0] and g2==t[1]:
                continue
            try:
                p = nx.shortest_path(G, source=g1, target=t[0])
            except NetworkXNoPath:
                continue
            l = len(p)
            print l, p
            if g2 in l:
                l -= 1
            if t[1] in l:
                l -= 1
            if min_len > l:
                min_len = l
        if min_len == 1:
            tp[1].append(gpair)
            continue
        elif min_len < 0x7fffffff:
            tp[2].append(gpair)
            continue
        flag = True
        for t in geneset_gt3:
            try:
                p = nx.shortest_path_length(G, source=g1, target=t[1])
            except NetworkXNoPath:
                continue
            flag = not flag
            tp[3].append(gpair)
            break
        if flag:
            tjfak.append(gpair)

    print "RESULT"
    for i in range(4):
        print tp[i]
    print tjfak


def merge_2node_cluster(geneset_2node, geneset_gt3):
    _geneset = []
    for gpair in geneset_2node:
        _geneset.extend(gpair)
    geneset = geneset_gt3
    geneset.append(_geneset)
    return geneset

def export_merged_geneset(geneset, n_name, dir="./"):
    f = open(dir + n_name + '_2node_removed.gmt', 'w')
    for i, glist in enumerate(geneset):
        f.write(str(i+1) + '\t' + n_name + '\t' + '\t'.join(glist) + '\n')
    f.close()


if __name__ =='__main__':
    network_list = []
    #network_list.append('1_1_ppi')
    network_list.append('2_ppi_anonym_v2')
    network_list.append('3_signal_anonym_directed_v3')
    #network_list.append('4_coexpr_anonym_v2')
    network_list.append('5_cancer_anonym_v2')
    network_list.append('6_homology_anonym_v2')
    for network_name in network_list:
        network_file = "Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge1/" + network_name + ".txt"
        geneset_file = "Q:/DreamChallenge-Disease Module Identification/Tools/COSSY/data/" + network_name + ".gmt"
        G=read_graph(network_file,network_type='undirected')
        geneset_list = read_genesetfile(geneset_file,input_format='gmt')
        geneset_2node, geneset_gt3 = separate_geneset_2node_or_not(geneset_list)
        #get_freq(geneset_2node, geneset_gt3, G)
        geneset_merged = merge_2node_cluster(geneset_2node, geneset_gt3)
        export_merged_geneset(geneset_merged, network_name, dir="Q:/DreamChallenge-Disease Module Identification/Tools/COSSY/data/")