__author__ = 'SungJoonPark'
import pandas as pd
import numpy as np
import random


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

def dropout_keep_topK_and_drop_remainder_uniformly(rootdir='./', network_file=None, expdir='dropout/', K=0.5, ratio = 0.2, cyc = 200):
    expdir = expdir + 'keeptop_' + str(K) + '_ratio_' + str(ratio) + '/'
    df = pd.read_csv(rootdir + network_file, sep="\t", header=None, names=['Node1', 'Node2', 'Weight'])
    df = df.sort_values('Weight', axis=0, ascending=False)

    boundary = int(len(df) * K)
    donotdrop = int((len(df) - boundary) * (ratio / (1 - K)))

    keep_idx = list(df.index[0:boundary])
    dropout_idx = list(df.index[boundary:])

    for i in range(cyc):
        random.shuffle(dropout_idx)
        exp_idx = keep_idx[:]
        exp_idx.extend(dropout_idx[0:donotdrop])
        df.loc[exp_idx].to_csv(rootdir+expdir+network_file+'_'+str(i)+'.txt', sep="\t", float_format="%.6f", header=False, index=False)



if __name__ =='__main__':
    rootdir = 'Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge2/integration/'
    networkfile = "1_2_3_topKpercentScalining_network_conf_keep_hightest.txt"
    dropout_keep_topK_and_drop_remainder_uniformly(rootdir = rootdir, network_file = networkfile, expdir='dropout/')

    # for i in range(200,201):
    #     output_filename = output_dir+"1_ppi_anonym_v2_dropout_"+str(i)+".txt"
    #     print output_filename
    #     regenerated_edge_list=dropout_style_regenerate_data(networkfile)
    #     write_edgelist(regenerated_edge_list,output_filename=output_filename)
