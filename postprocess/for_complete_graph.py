__author__ = 'SungJoonPark'
import pandas as pd
import random

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

    print cluster_size

def divide_list_by_cluster_num(list_, cluster_num):
    #split list by chunk size
    if len(list_)<cluster_num:
        raise Exception('cluster num is larger than list length')
    splited_list = []
    bin = len(list_) / cluster_num


    for chunk in range(1,cluster_num+1):
        if chunk == 1:
            splited_list.append(list_[0:bin])
        elif chunk == cluster_num:
            splited_list.append(list_[bin*(chunk-1):])
        else:
            splited_list.append(list_[bin*(chunk-1):(bin*(chunk-1))+bin])
    return splited_list

def get_large_module_divided_genset_list(geneset_list):
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

if __name__ =='__main__':
    node_list = ['a','b','c','d','e','f','g']
    shuffled_node_list= shuffle_nodes(node_list)
    get_appropriate_cluster_size_for_challenge(range(101))