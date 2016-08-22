__author__ = 'SungJoonPark'

import pandas as pd
import os

def ChallengeDataFormatToCossyInput(filename, output_folder_path,output_name):
    if not os.path.exists(output_folder_path+output_name):
        os.makedirs(output_folder_path+output_name)

    df = pd.read_csv(filename,sep='\t',header=None)

    edge_df = df[[0,1]]
    edge_df = edge_df.astype(int)
    edge_df = edge_df + 1
    edge_df.to_csv(output_folder_path+output_name+"/edge-"+output_name+".txt", header=False, index=False,sep='\t')


    node_list  = sorted(list(set(df[0]).union(set(df[1]))))
    node_df = pd.DataFrame()
    node_df[0] = node_list
    node_df[1] = node_list
    node_df = node_df.astype(int)
    node_df = node_df+1

    node_df.to_csv(output_folder_path+output_name+"/node-"+output_name+".txt",header=False, index=False , sep='\t')

    w= open(output_folder_path+output_name+"/"+output_name+".txt",'w')
    w.write(output_name)
    w.write('\n')
    w.close()

ChallengeDataFormatToCossyInput("F:/PycharmProject/DMI/subgraph_1.txt","F:/PycharmProject/DMI/","1_1")
ChallengeDataFormatToCossyInput("F:/PycharmProject/DMI/subgraph_498.txt","F:/PycharmProject/DMI/","1_498")
ChallengeDataFormatToCossyInput("F:/PycharmProject/DMI/subgraph_587.txt","F:/PycharmProject/DMI/","1_587")