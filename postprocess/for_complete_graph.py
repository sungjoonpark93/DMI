__author__ = 'SungJoonPark'
import pandas as pd
import random
from sklearn.cross_validation import KFold
import base

def shuffle_nodes(node_list):
    copy_node_list = node_list[:]
    random.shuffle(copy_node_list)
    return copy_node_list

def get_appropriate_cluster_size_for_challenge(node_list):
    if len(node_list)<=100:
        raise Exception('inapproprate node_list length')
    total_node_num = len(node_list)
    moc = total_node_num / 100
    namuzee = total_node_num % 100.0
    if namuzee>0:
        cluster_size = moc+1
    elif namuzee==0:
        cluster_size = moc

    return cluster_size


def divide_list_by_cluster_num(list_, cluster_num):
    #split list by chunk size
    if len(list_)<cluster_num:
        raise Exception('cluster num is larger than list length')
    splited_list = []

    def split_seq(seq, p):
        newseq = []
        n = len(seq) / p    # min items per subsequence
        r = len(seq) % p    # remaindered items
        b,e = 0, n + min(1, r)  # first split
        for i in range(p):
            newseq.append(seq[b:e])
            r = max(0, r-1)  # use up remainders
            b,e = e, e + n + min(1, r)  # min(1,r) is always 0 or 1

        return newseq

    splited_list = split_seq(list_, cluster_num)

    return splited_list


def get_large_module_divided_genset_list(geneset_list):
    #input geneset_list, one element is a one genset
    large_module_divided_geneset_list = []
    for geneset in geneset_list:
        if len(geneset)<=100:
            large_module_divided_geneset_list.append(geneset)
        elif len(geneset)>100:
            appropriate_cluster_size = get_appropriate_cluster_size_for_challenge(geneset)
            shuffled_geneset = shuffle_nodes(geneset)

            divided_geneset_list = divide_list_by_cluster_num(shuffled_geneset,cluster_num=appropriate_cluster_size)
            for divided_geneset in divided_geneset_list:
                large_module_divided_geneset_list.append(divided_geneset)
    return large_module_divided_geneset_list


def run(input_genset_file=None,input_format='gmt' , output_geneset_file=None,output_format='challenge'):
    #get input genset file and divide randomly lager
    geneset_list = base.read_genesetfile(genesetfile=input_genset_file,input_format=input_format)
    large_module_divided_genset_list = get_large_module_divided_genset_list(geneset_list)
    base.write_genesetfile(large_module_divided_genset_list,outputfile=output_geneset_file, output_format=output_format)

if __name__ =='__main__':
    input_geneset_file = "Q:\DreamChallenge-Disease Module Identification\Tools\COSSY\data/1_ppi_anonym_v2.gmt"
    output_geneset_file = "Q:\DreamChallenge-Disease Module Identification\Tools\COSSY\data/1_ppi_anonym_v2_submission_test.gmt"
    run(input_genset_file=input_geneset_file,input_format='gmt',output_geneset_file=output_geneset_file,output_format='challenge')