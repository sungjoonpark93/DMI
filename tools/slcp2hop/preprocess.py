__author__ = "WonhoShin"

import numpy as np
import pandas as pd

def cutoffEdgesByThreshold(rootdir="./", expdir="", file=None, deli='\t', critcol=2, method='PERCENT', th=0.3, expfmt='binary'):

    #read network info
    df_edges = pd.read_csv(rootdir+file, header=None, sep="\t")

    #filtering edges
    if method == 'STDEV':
        print df_edges[2].mean()
        print df_edges[2].std()
        #tq vywnsvusck Qoaus skasmsrp djqtdma
    elif method == 'PERCENT':
        df_res = df_edges.sort_values([2], ascending=False).iloc[0:int(1 - len(df_edges) * th)]
        if expfmt == 'binary':
            df_res = df_res.drop([2], axis=1)
        tot_nodes = len(list(set(df_res[0].tolist()) | set(df_res[1].tolist())))
        df_res.to_csv(rootdir + expdir + file + "_" + method + "_" + str(th) + "_dropped_" + expfmt + "_" + str(tot_nodes) + ".txt", sep="\t", index=False, header=False, float_format="%.5f")
    elif method == 'ABS':
        df_res = df_edges[(df_edges[2] >= th)]
        if expfmt == 'binary':
            df_res = df_res.drop([2], axis=1)
        tot_nodes = len(list(set(df_res[0].tolist()) | set(df_res[1].tolist())))
        df_res.to_csv(rootdir + expdir + file + "_" + method + "_" + str(th) + "_dropped_" + expfmt + "_" + str(tot_nodes) + ".txt", sep="\t", index=False, header=False, float_format="%.5f")
    else:
        do = "SOMETHING"

rootdir = "Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1\\"
file_list = [
    #"1_ppi_anonym_v2.txt",
    #"2_ppi_anonym_v2.txt",
    #"3_signal_anonym_directed_v3.txt_duplicates_removed.txt",
    #"4_coexpr_anonym_v2.txt",
    #"5_cancer_anonym_v2.txt",
    "6_homology_anonym_v2.txt"
]

if __name__ == "__main__":
    for f in file_list:
        for th in [0.5, 0.7, 0.8]:
            cutoffEdgesByThreshold(rootdir=rootdir, file=f, method='PERCENT', expdir="abs\\", th=th, expfmt="binary")