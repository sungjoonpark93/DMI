__author__ = 'SungJoonPark'
import pandas as pd
import networkx as nx

def read_graph(network_file=None):
    #to cover directed, and undirected graph we use directed graph.
    G = nx.DiGraph()
    df = pd.read_csv(network_file,sep="\t", header=None, names=['Node1','Node2','Weight'])
    #Node label should be string not integer even is integer!
    edge_list =[(str(row[0]),str(row[1]),row[2]) for row in df.values]
    G.add_weighted_edges_from(edge_list)

    return G


def read_genesefile(genesetfile=None,filter_thr=100,input_format="txt"):
    geneset_list = []
    with open(genesetfile,'r') as r:
        for line in r:
            if input_format =='txt':
                #Node label should be string not integer even is integer!
                geneset_list.append(line.strip().split("\t"))
            elif input_format =='gmt':
                #Node label should be string not integer even is integer!
                geneset_list.append(line.strip().split("\t")[2:])
    geneset_list = [gene_list for gene_list in geneset_list if len(gene_list)>filter_thr]
    return geneset_list


def get_subgraph(G, geneset_list):
    SG_dict = {}
    for i,geneset in enumerate(geneset_list):
        SG = G.subgraph(geneset)
        SG_dict[i] = SG.edges(data=True)

    return SG_dict

def output_subgraph_to_file(SG_dict,outputfolder=None):
    for cluster_id in SG_dict.keys():
        outputfile = outputfolder+"subgraph_"+str(cluster_id)+".txt"

        w = open(outputfile,'w')
        edge_list = SG_dict[cluster_id]
        for edge in edge_list:
            #edge weight should considered
            w.write(edge[0]+"\t"+edge[1]+"\t"+str(edge[2]['weight'])+"\n")
        w.close()


if __name__ =='__main__':
    network_file = "Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge1/3_signal_anonym_directed_v3.txt"
    geneset_file = "Q:/DreamChallenge-Disease Module Identification/Tools/COSSY/data/1_3_signal.gmt"
    G=read_graph(network_file)
    geneset_list = read_genesefile(geneset_file,input_format='gmt',filter_thr=100)
    SG_dict = get_subgraph(G,geneset_list)
    output_subgraph_to_file(SG_dict,"./")
