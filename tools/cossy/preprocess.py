__author__ = 'SungJoonPark'

import pandas as pd
import os

def ChallengeDataFormatToCossyInput(filename, output_folder_path,output_name):
    if not os.path.exists(output_folder_path+output_name):
        os.makedirs(output_folder_path+output_name)

    df = pd.read_csv(filename,sep='\t',header=None)

    edge_df = df[[0,1]]
    edge_df = edge_df.astype(int)
    #we need to -1 when the cossy result is gotton
    edge_df = edge_df+1



    node_list  = sorted(list(set(df[0]).union(set(df[1]))))
    node_df = pd.DataFrame()
    node_df[0] = node_list
    node_df[1] = node_list
    node_df = node_df.astype(int)
    #we need to -1 when the cossy result is gotton
    node_df[0] = node_df[0]+1



    edge_df.to_csv(output_folder_path+output_name+"/edge-"+output_name+".txt", header=False, index=False,sep='\t')
    node_df.to_csv(output_folder_path+output_name+"/node-"+output_name+".txt",header=False, index=False , sep='\t')

    w= open(output_folder_path+output_name+"/"+output_name+".txt",'w')
    w.write(output_name)
    w.write('\n')
    w.close()


# ChallengeDataFormatToCossyInput("F:/PycharmProject/DMI/subgraph_1.txt","F:/PycharmProject/DMI/","1_1")
# ChallengeDataFormatToCossyInput("F:/PycharmProject/DMI/subgraph_498.txt","F:/PycharmProject/DMI/","1_498")
# ChallengeDataFormatToCossyInput("F:/PycharmProject/DMI/subgraph_587.txt","F:/PycharmProject/DMI/","1_587")

def ChallengeDataFormatToCossyInput_2(filename, output_folder_path,output_name):
    if not os.path.exists(output_folder_path+output_name):
        os.makedirs(output_folder_path+output_name)

    df = pd.read_csv(filename,sep='\t',header=None)
    node_list  = sorted(list(set(df[0]).union(set(df[1]))))
    local_id_list = range(1,len(node_list)+1)

    node_df = pd.DataFrame()
    node_df[0]=local_id_list
    node_df[1]=node_list
    node_df = node_df.astype(int)

    mapping_dict = node_df.set_index(1)[0]


    edge_df = df[[0,1]]
    edge_df = edge_df.astype(int)
    edge_df[0] =  mapping_dict[edge_df[0].values].values
    edge_df[1] =  mapping_dict[edge_df[1].values].values


    edge_df.to_csv(output_folder_path+output_name+"/edge-"+output_name+".txt", header=False, index=False,sep='\t')
    node_df.to_csv(output_folder_path+output_name+"/node-"+output_name+".txt",header=False, index=False , sep='\t')

    w= open(output_folder_path+output_name+"/"+output_name+".txt",'w')
    w.write(output_name)
    w.write('\n')
    w.close()


if __name__ =='__main__':


    ChallengeDataFormatToCossyInput_2("Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1\high_degree_node_removed/1_top3_nodes_removed_network.txt","Q:\DreamChallenge-Disease Module Identification\Tools\COSSY\data/networks/","1_top3_nodes_removed_network")
    ChallengeDataFormatToCossyInput_2("Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1\high_degree_node_removed/1_top50_nodes_removed_network.txt","Q:\DreamChallenge-Disease Module Identification\Tools\COSSY\data/networks/","1_top50_nodes_removed_network")
    ChallengeDataFormatToCossyInput_2("Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1\high_degree_node_removed/1_top100_nodes_removed_network.txt","Q:\DreamChallenge-Disease Module Identification\Tools\COSSY\data/networks/","1_top100_nodes_removed_network")
    ChallengeDataFormatToCossyInput_2("Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1\high_degree_node_removed/1_top300_nodes_removed_network.txt","Q:\DreamChallenge-Disease Module Identification\Tools\COSSY\data/networks/","1_top300_nodes_removed_network")
    #reconstructedNetorktoCossyinput("F:/PycharmProject/DMI/subgraph_1.txt","./","1_1_1")
    #ChallengeDataFormatToCossyInput_2("Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1/6_homology_anonym_v2.txt","Q:\DreamChallenge-Disease Module Identification\Tools\COSSY\data/networks/", "1_6_homology_modified")
    #ChallengeDataFormatToCossyInput_2("Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1/6_homology_anonym_v2.txt","Q:\DreamChallenge-Disease Module Identification\Tools\COSSY\data/networks/", "1_6_homology_modified")