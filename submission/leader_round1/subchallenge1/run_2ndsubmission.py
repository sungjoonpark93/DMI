__author__ = 'SungJoonPark'
__author__ = 'SungJoonPark'
import base


input_root_dir = "Q:\DreamChallenge-Disease Module Identification\Tools\SPICi\SPICi\output\leaderboard_round1_sub1_2nd_submission/"
output_root_dir ="Q:\DreamChallenge-Disease Module Identification\Submission\Leaderboard_round1\Subchallenge1/"
dataset = {'1_ppi_anonym_v2.txt':"1_ppi_anonym_v2_d_0.5_s_3_m_1_.txt_2node_removed.gmt_gt100_separated_811.gmt" ,
           '2_ppi_anonym_v2.txt':"2_ppi_anonym_v2_d_0.5_s_3_m_1_.txt_2node_removed.gmt_gt100_separated_1057.gmt",
          '3_signal_anonym_directed_v3.txt':"3_signal_anonym_directed_v3.txt_normalized_0to1_top_0.150.txt_duplicates_removed_d_0.5_s_3_m_1_.txt_2node_removed.gmt_gt100_separated_206.gmt",
          '4_coexpr_anonym_v2.txt' :'4_coexpr_anonym_v2_d_0.5_s_3_m_1_.txt_2node_removed.gmt_gt100_separated_36.gmt',
          '5_cancer_anonym_v2.txt' : '5_cancer_anonym_v2_d_0.5_s_3_m_1_.txt_2node_removed.gmt_gt100_separated_152.gmt',
          '6_homology_anonym_v2.txt' : '6_homology_anonym_v2.txt_normalized_0to1_top_0.150_d_0.5_s_3_m_1_.txt_2node_removed.gmt_gt100_separated_381.gmt'}

for data in dataset.keys():
    base.convert_genesetfile_format(input_genestfile=input_root_dir+dataset[data], input_format='gmt', outputfile=output_root_dir+data)