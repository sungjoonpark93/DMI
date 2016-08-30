__author__ = 'SungJoonPark'
import pandas as pd
import numpy as np


def write_edgelist(edge_list, output_filename):
    w= open(output_filename,'w')
    for edge in edge_list:
        w.write(edge[0]+"\t"+edge[1]+"\t"+str(edge[2])+"\n")
    w.close()

def dropout_style_regenerate_data(networkfile,edge_prob='conf'):
    df = pd.read_csv(networkfile,sep="\t", header=None, names=['Node1','Node2','Weight'])
    index_list = list(df.index)

    edge_list =[(str(int(row[0])),str(int(row[1])),row[2]) for row in df.values]
    if edge_prob=='conf':
        #prob_list is weight_list in which the value is confidence score 0~1
        prob_list = list(df['Weight'].values)
        regenerated_edge_list = []
        for edge in edge_list:
            is_chosen = np.random.choice([True,False],p=[edge[2],1-edge[2]])
            if is_chosen ==True:
                regenerated_edge_list.append(edge)


    return regenerated_edge_list


if __name__ =='__main__':
    networkfile = "Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1/1_ppi_anonym_v2.txt"
    output_dir = "Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1\dropout_style/1_ppi_anonym_v2/"
    for i in range(200,201):
        output_filename = output_dir+"1_ppi_anonym_v2_dropout_"+str(i)+".txt"
        print output_filename
        regenerated_edge_list=dropout_style_regenerate_data(networkfile)
        write_edgelist(regenerated_edge_list,output_filename=output_filename)
