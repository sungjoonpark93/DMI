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

    dataset_list = ["1_ppi_anonym_v2","2_ppi_anonym_v2.txt","3_signal_anonym_directed_v3.txt_duplicates_removed.txt","4_coexpr_anonym_v2.txt",
                    "5_cancer_anonym_v2.txt","6_homology_anonym_v2.txt_normalized_0to1_top_0.150.txt"]

    input_dir = "Q:\DreamChallenge-Disease Module Identification\Tools\MLR-MCL\mlrmcl1.2\data\subchallenge1\leaderboard_round1_3rd_submission/"
    inputfile_list = map(lambda x : input_dir+x, dataset_list)

    output_dir = "Q:\DreamChallenge-Disease Module Identification\Tools\MLR-MCL\mlrmcl1.2\data\subchallenge1\leaderboard_round1_3rd_submission/"
    outputfile_list = map(lambda x:output_dir + os.path.splitext(x)[0]+"unweighted_.graph", dataset_list)

    for i,inputfile in enumerate(inputfile_list):
        print inputfile, outputfile_list[i]
        MLRMCLoutputfile_to_gmtfile(inputfile,outputfile_list[i])

