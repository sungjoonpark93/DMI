__author__ = 'WonhoShin'
import pandas as pd
import numpy as np

network_info = [
    {"dir":"Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge2/"},
    {
        "dir": "Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge2/",
        "fname": "1_ppi_anonym_aligned_v2.txt",
        "th": 0.0
    },
    {
        "dir": "Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge2/",
        "fname": "2_ppi_anonym_aligned_v2.txt",
        "th": 0.0
    },
    {
        "dir": "Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge2/",
        "fname": "3_signal_anonym_aligned_directed_v3.txt",
        "th": 0.0
    },
    {
        "dir": "Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge2/",
        "fname": "4_coexpr_anonym_aligned_v2.txt",
        "th": 0.0
    },
    {
        "dir": "Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge2/",
        "fname": "5_cancer_anonym_aligned_v2.txt",
        "th": 0.0
    },
    {
        "dir": "Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge2/",
        "fname": "6_homology_anonym_aligned_v2.txt",
        "th": 0.0
    }
]

def cmp_numeric_id(s1, s2):
    return int(s1) < int(s2)

def open_network_files(finfo):
    xy = np.genfromtxt(finfo['dir'] + finfo['fname'], dtype='str', unpack=True, skip_header=0,
                       delimiter='\t')
    lb = []
    for i in range(len(xy[0])):
        s = None
        if cmp_numeric_id(xy[0][i], xy[1][i]):
            s = xy[0][i] + '_' + xy[1][i]
        else:
            s = xy[1][i] + '_' + xy[0][i]
        lb.append(s)

    _df = pd.DataFrame(data=xy[2], index=lb, columns=[finfo['fname']], dtype=np.float32)
    df = _df[_df[finfo['fname']] > finfo['th']]
    df = df[~df.index.duplicated(keep='first')]
    return df

def get_network_as_df_freq(flist = range(1,7)):
    df_list = []
    df_idx = []
    for f in flist:
        df_list.append(open_network_files(network_info[f]))
        df_idx = list(set(df_idx).union(set(df_list[-1].index)))
    df = pd.concat(df_list, axis=1)
    df.to_csv('whole_network.tsv', sep='\t')
    #print df.isnull().sum(axis=1)
    df.count(axis=1).to_frame().div(6.0, axis=1).to_csv('whole_network_freq.tsv', sep='\t')
    #f = open('whole_network.txt', 'w')
    #for e in df_idx:
    #    f.write(e.replace('_', '\t') + '\t1\n')

def get_network_as_df_conf_avg(flist = range(1,7)):
    df_list = []
    df_idx = []
    norm_list = [3,6]
    for f in flist:
        df_list.append(open_network_files(network_info[f]))
        if f in norm_list:
            divval = df_list[-1].max(axis=0)[network_info[f]['fname']]
            print divval
            df_list[-1] = df_list[-1].div(divval, axis=1)
        df_idx = list(set(df_idx).union(set(df_list[-1].index)))
    df = pd.concat(df_list, axis=1)
    df.to_csv('whole_network.tsv', sep='\t')
    #print df.isnull().sum(axis=1)
    #df.fillna(value=0).mean(axis=1).to_csv('whole_network_conf_avg.tsv', sep='\t')
    df.mean(axis=1).to_csv('whole_network_conf_avg.tsv', sep='\t')
    #f = open('whole_network.txt', 'w')
    #for e in df_idx:
    #    f.write(e.replace('_', '\t') + '\t1\n')



if __name__ == "__main__":
    #get_network_as_df()
    get_network_as_df_conf_avg()
    #df1 = pd.DataFrame({'A': [1, 2, 1]}, index=[0, 1, 3])
    #df2 = pd.DataFrame({'B': [1, 2, 1]}, index=[0, 3, 4])
    #print df1
    #print df2
    #df = pd.concat([df1, df2], axis=1)
    #print df