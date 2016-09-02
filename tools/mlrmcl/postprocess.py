__author__ = 'SungJoonPark'
import pandas as pd
import os


def MLRMCLoutputfile_to_gmtfile(MLRMCLoutputfile, gmtfile):
    cluster_dict={}
    with open(MLRMCLoutputfile,'r') as r:
        for i,line in enumerate(r):
            node_id = i
            cluster_id = int(line.strip())
            if cluster_id not in cluster_dict:
                cluster_dict[cluster_id] = [node_id]
            else:
                cluster_dict[cluster_id].append(node_id)

    with open(gmtfile,'w') as w:
        for cluster_id in sorted(cluster_dict.keys()):
            w.write(str(cluster_id+1)+"\t"+"0.5"+"\t")
            for node in cluster_dict[cluster_id]:
                w.write(str(node)+"\t")
            w.write("\n")


if __name__ =='__main__':

    dataset_list = ["1_ppi_anonym_v2_b_1_c_17397_i_2.out","2_ppi_anonym_v2_b_1_c_2000_i_2.out","3_signal_anonym_directed_v3.txt_duplicates_removed_b_1_c_5254_i_2.out",
                    "4_coexpr_anonym_v2_b_1_c_12588_i_2.out","5_cancer_anonym_v2_b_1_c_14679_i_2.out","6_homology_anonym_v2_reindex_b_1_c_10405_i_2.out"]

    input_dir = "Q:\DreamChallenge-Disease Module Identification\Tools\MLR-MCL\mlrmcl1.2\output\subchallenge1\leaderboard_round1_3rd_submission/"
    inputfile_list = map(lambda x : input_dir+x, dataset_list)

    output_dir = input_dir
    outputfile_list = map(lambda x:output_dir + os.path.splitext(x)[0]+".gmt", dataset_list)

    for i,inputfile in enumerate(inputfile_list):
        print inputfile, outputfile_list[i]
        MLRMCLoutputfile_to_gmtfile(inputfile,outputfile_list[i])

