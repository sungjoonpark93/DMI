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

def separate_geneset_hub_or_not(G, geneset_list):
    geneset_hub = []
    geneset_etc = []
    for geneset in geneset_list:
        if len(geneset) <= 100:
            geneset_etc.append(geneset)
            continue
        _G = G.subgraph(geneset)
        if len([x for x in geneset if _G.degree(x) == 1]) > int(0.7 * len(geneset)):
            geneset_hub.append(geneset)
        else:
            geneset_etc.append(geneset)
    return geneset_hub, geneset_etc


def separate_geneset_gt100_or_not(geneset_list):
    geneset_gt100 = [x for x in geneset_list if len(x) >100]
    geneset_etc = [x for x in geneset_list if len(x) <= 100]
    return geneset_gt100, geneset_etc

def cutoff_hub_cluster(_G=None, geneset=None):
    # edge_list = nx.edges(G, nbunch=geneset, data=True)
    G = _G.subgraph(geneset)
    edge_list = G.edges(data=True)
    edge_list = sorted(edge_list, key = lambda x: x[2]['weight'])
    for e in edge_list:
        _e = None
        if G.degree(e[0]) < G.degree(e[1]):
            _e = e[0]
        else:
            _e = e[1]
        if _e in geneset:
            geneset.remove(_e)
        if len(geneset) <= 100:
            break;
    return [geneset]



def separate_gt100_cluster(G=None, geneset=None):
    sep_geneset = []
    k = len(geneset)/100
    if len(geneset)%100:
        k += 1
    cluster_size = len(geneset) / k
    sep_boundary = [x *( cluster_size) for x in range(k)]
    sep_boundary.append(len(geneset))
    _geneset = sorted(geneset, key = lambda x: G.degree(x), reverse=True)
    for i in range(len(sep_boundary) - 1):
        sep_geneset.append(_geneset[sep_boundary[i]:sep_boundary[i+1]])
    return sep_geneset

def merge_separated_cluster(_geneset, geneset_sep):
    geneset = _geneset
    geneset.extend(geneset_sep)
    return geneset

def export_merged_geneset(geneset, network_name, geneset_file):
    f = open(geneset_file + '_gt100_separated.gmt', 'w')
    for i, glist in enumerate(geneset):
        f.write(str(i+1) + '\t' + network_name + '\t' + '\t'.join(glist) + '\n')
    f.close()

def run(network_file, network_name, geneset_file, geneset_fmt):
    G = read_graph(network_file, network_type='undirected')
    geneset_list = read_genesetfile(geneset_file, input_format=geneset_fmt)

    geneset_hub, geneset = separate_geneset_hub_or_not(G, geneset_list)
    for sub_geneset in geneset_hub:
        geneset = merge_separated_cluster(geneset, cutoff_hub_cluster(G, sub_geneset))

    geneset_gt100, geneset = separate_geneset_gt100_or_not(geneset)
    for sub_geneset in geneset_gt100:
        geneset = merge_separated_cluster(geneset, separate_gt100_cluster(G, sub_geneset))

    export_merged_geneset(geneset, network_name, geneset_file)

if __name__ =='__main__':
    network_list = []
    network_list.append(['1_ppi_anonym_aligned_v2', 'Q:\DreamChallenge-Disease Module Identification\Tools\SPICi\SPICi\output\subchallenge2\conf_avg_10_0.5.txt_2node_removed.gmt'])
    # network_list.append(['1_ppi_anonym_v2', 'postprocessed/1_ppi_6934_removed_network_6934_reassigned_2node_removed'])
    # network_list.append(['2_ppi_anonym_v2', 'postprocessed/2_ppi_anonym_v2_2node_removed'])
    # network_list.append(['3_signal_anonym_directed_v3', 'postprocessed/3_signal_anonym_directed_v3_2node_removed'])
    # network_list.append(['4_coexpr_anonym_v2', 'postprocessed/4_coexpr_anonym_v2_2node_removed'])
    # network_list.append(['5_cancer_anonym_v2', 'postprocessed/5_cancer_anonym_v2_2node_removed'])
    # network_list.append(['6_homology_anonym_v2', 'postprocessed/6_homology_anonym_v2_2node_removed'])
    for network_name, geneset_name in network_list:
        network_file = "Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge2/" + network_name + ".txt"
        #geneset_file = "Q:/DreamChallenge-Disease Module Identification/Tools/COSSY/data/" + geneset_name + ".gmt"
        geneset_file = geneset_name
        G=read_graph(network_file,network_type='undirected')
        geneset_list = read_genesetfile(geneset_file,input_format='gmt')

        geneset_hub, geneset = separate_geneset_hub_or_not(G, geneset_list)
        for sub_geneset in geneset_hub:
            geneset = merge_separated_cluster(geneset, cutoff_hub_cluster(G, sub_geneset))

        geneset_gt100, geneset = separate_geneset_gt100_or_not(geneset)
        for sub_geneset in geneset_gt100:
            geneset = merge_separated_cluster(geneset, separate_gt100_cluster(G, sub_geneset))

        export_merged_geneset(geneset, network_name, geneset_name, dir="Q:/DreamChallenge-Disease Module Identification/Tools/COSSY/data/")
