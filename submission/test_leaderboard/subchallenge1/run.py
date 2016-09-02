__author__ = 'SungJoonPark'
import base


input_root_dir = "Q:\DreamChallenge-Disease Module Identification\Tools\COSSY\data\sub1_res/"
output_root_dir ="Q:\DreamChallenge-Disease Module Identification\Submission/test_leaderboard/subchallenge1/"
dataset = {'1_ppi_anonym_v2.txt':"1_ppi_6934_removed_network_6934_reassigned_2node_removed_gt100_separated.gmt" ,
           '2_ppi_anonym_v2.txt':"2_ppi_anonym_v2_2node_removed_gt100_separated.gmt",
          '3_signal_anonym_directed_v3.txt':"3_signal_anonym_directed_v3_2node_removed_gt100_separated.gmt",
          '4_coexpr_anonym_v2.txt' :'4_coexpr_anonym_v2_2node_removed_gt100_separated.gmt',
          '5_cancer_anonym_v2.txt' : '5_cancer_anonym_v2_2node_removed_gt100_separated.gmt',
          '6_homology_anonym_v2.txt' : '6_homology_anonym_v2_2node_removed_gt100_separated.gmt'}

for data in dataset.keys():
    base.convert_genesetfile_format(input_genestfile=input_root_dir+dataset[data], input_format='gmt', outputfile=output_root_dir+data)