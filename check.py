__author__ = 'SungJoonPark'

import pandas as pd

def check_is_overlapped(challengefile):
    count_dict = {}
    with open(challengefile,'r') as r:
        for line in r:
            line_list = line.strip().split("\t")
            clsuter_id = line_list[0]
            geneset = line_list[2:]
            for gene in geneset:
                #print gene
                if gene not in count_dict:
                    count_dict[gene]=1
                else:
                    count_dict[gene]=count_dict[gene]+1
                    #print clsuter_id, gene
                    raise Exception("overlapped!!")
    print "it's okay!"

if __name__ =='__main__':
    check_is_overlapped("Q:\DreamChallenge-Disease Module Identification\Tools\WGCNA\output\leaderboard_round1_4thsubmission/4_coexpr_anonym_v2_minModuleSize5_deepSplit4.txt")