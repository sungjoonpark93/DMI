__author__ = "WonhoShin"

rootdir = "Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge2\integration\dropout\keeptop_0.5_ratio_0.2\\"
#rootdir = "Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge2\\"

network_list = [
    #"2_ppi_anonym_aligned_v2.txt"
    # "whole_network_conf_keep_highest.txt"
    # "1_ppi_anonym_v2.txt",
    # "2_ppi_anonym_v2.txt",
    # "3_signal_anonym_directed_v3.txt_duplicates_removed.txt",
    # "4_coexpr_anonym_v2.txt",
    # "5_cancer_anonym_v2.txt",
    # "6_homology_anonym_v2.txt"
    #"subchallenge2/1_2_3_network_conf_keep_highest.txt"
]

for i in range(200):
    network_list.append("1_2_3_topKpercentScalining_network_conf_keep_hightest.txt_" + str(i) + ".txt")
    #network_list.append("5_cancer_anonym_v2.txt_" + str(i) + ".txt")
    #network_list.append("6_homology_anonym_v2.txt_" + str(i) + ".txt")

for fname in network_list:
    f = open(rootdir + fname, "r")
    fout = open(rootdir + "bin\\" + fname + "_bin.txt", "w")
    while True:
        line = f.readline()
        if not line:
            break
        fout.write(" ".join(line.split("\t")[:2]) + "\n")
    f.close()
    fout.close()
