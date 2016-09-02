__author__ = 'SungJoonPark'
import base

#submitted version. but we did wrong. we used 1_1_ppi
# inputfilename = "Q:\DreamChallenge-Disease Module Identification\Tools\SPICi\SPICi\output\subchallenge2\dropout\similarity_score_and_divided_by_200/similarity_score_info_result.txt_2node_removed.gmt_gt100_separated.gmt"
# outputfilename = "Q:\DreamChallenge-Disease Module Identification\Submission\TestLeaderboard\Subchallenge2/predicted_modules_subchallenge2.txt"
# base.convert_genesetfile_format(input_genestfile=inputfilename, input_format='gmt', outputfile=outputfilename)

#we prepared for another submission but
inputfilename = "Q:\DreamChallenge-Disease Module Identification\Tools\SPICi\SPICi\output\subchallenge2\conf_avg_10_0.5.txt_2node_removed.gmt_gt100_separated.gmt"
outputfilename = "Q:\DreamChallenge-Disease Module Identification\Submission\TestLeaderboard\Subchallenge2_hopeagain/predicted_modules_subchallenge2.txt"
base.convert_genesetfile_format(input_genestfile=inputfilename, input_format='gmt', outputfile=outputfilename)