__author__ = 'SungJoonPark'
import pandas as pd

def cut_off_edge(networkfile=None, low_k_percent = 50,outputfile=None):
    # remove low k number of edge

    df = pd.read_csv(networkfile,sep="\t", header=None, names=['Node1','Node2','Weight'])
    cut_k = int((len(df.index) * (low_k_percent*0.01)))+1
    print len(df.index)
    print cut_k
    sorted_df_by_weight = df.sort_values('Weight',axis=0)
    if cut_k >= len(sorted_df_by_weight.index):
        raise Exception('low_k is larger than total edge number')
    cut_off_df =  sorted_df_by_weight.iloc[cut_k:,:]

    cut_off_df_edge_order_preserved =  cut_off_df.sort_index()

    cut_off_df_edge_order_preserved.to_csv(outputfile,sep="\t",index=False,header=False)
if __name__ =='__main__':
    low_k_percent = 99
    outputfile = "Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1\edge_filtering/1_ppi_anonym_v2/1_ppi_anonym_v2"+"_low_"+str(low_k_percent)+"percent_edge_removed.txt"
    cut_off_edge("Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1/1_ppi_anonym_v2.txt",low_k_percent=low_k_percent, outputfile=outputfile)
