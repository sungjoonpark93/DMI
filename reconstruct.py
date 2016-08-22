__author__ = 'SungJoonPark'
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


def read_genesefile(genesetfile=None,input_format="txt"):
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


def get_induced_subgraph(G, geneset_list):
    SG_dict = {}
    for i,geneset in enumerate(geneset_list):
        SG = G.subgraph(geneset)
        print SG.number_of_edges()
        print SG.number_of_nodes()
        SG_dict[i] = SG.edges(data=True)

    return SG_dict

def get_subgraph(G, geneset_list,thr=100):
    SG_dict = {}
    for i,geneset in enumerate(geneset_list):
        edge_list= []
        if len(geneset)>thr:
            for j,node1 in enumerate(geneset):
                for node2 in geneset[(j+1):]:
                    #print node1,node2
                    if G.has_edge(node1,node2):
                        edge_weight = G.get_edge_data(node1,node2)
                        edge_list.append((node1,node2,edge_weight))
                    if G.has_edge(node2,node1):
                        edge_weight = G.get_edge_data(node2,node1)
                        edge_list.append((node2,node1,edge_weight))
            SG_dict[i] = edge_list

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
    network_file = "Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge1/1_ppi_anonym_v2.txt"
    geneset_file = "Q:/DreamChallenge-Disease Module Identification/Tools/COSSY/data/1_1_ppi.gmt"
    G=read_graph(network_file,network_type='directed')
    geneset_list = read_genesefile(geneset_file,input_format='gmt')
    SG_dict = get_subgraph(G,geneset_list, thr=100)
    output_subgraph_to_file(SG_dict,outputfolder="./")



