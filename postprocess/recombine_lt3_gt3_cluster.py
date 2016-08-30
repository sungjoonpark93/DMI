__author__ = "WonhoShin"

import argparse
import merge_2node_cluster as merge2
import separate_gt100_cluster as sep100

net_dict = {
    '1': {
        '1': 'Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge1/1_ppi_anonym_v2.txt',
        '2': 'Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge1/2_ppi_anonym_v2.txt',
        '3': 'Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge1/3_signal_anonym_directed_v3.txt',
        '4': 'Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge1/4_coexpr_anonym_v2.txt',
        '5': 'Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge1/5_cancer_anonym_v2.txt',
        '6': 'Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge1/6_homology_anonym_v2.txt'
    },
    '2': {
        '1': 'Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge2/1_ppi_anonym_aligned_v2.txt',
        '2': 'Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge2/2_ppi_anonym_aligned_v2.txt',
        '3': 'Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge2/3_signal_anonym_aligned_directed_v3.txt',
        '4': 'Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge2/4_coexpr_anonym_aligned_v2.txt',
        '5': 'Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge2/5_cancer_anonym_aligned_v2.txt',
        '6': 'Q:/DreamChallenge-Disease Module Identification/ChallengeData/subchallenge2/6_homology_anonym_aligned_v2.txt'
    }
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-sub', type=str, default=1, help='Subchallenge#')
    parser.add_argument('-net', type=str, default=1, help='Network#')
    parser.add_argument('-i', type=str, help="Input file path(geneset data)")
    parser.add_argument('-fmt', type=str, default='gmt', help="Format of Input file/ gmt(default)/ txt")

    #args = parser.parse_args()
    args = parser.parse_args(['-sub','2','-net','1','-i','Q:\DreamChallenge-Disease Module Identification\Tools\SPICi\SPICi\output\subchallenge2\conf_avg_10_0.5.txt','-fmt','txt'])

    network_file = net_dict[args.sub][args.net]
    geneset_file = args.i
    geneset_fmt = args.fmt

    merge2.run(network_file, 'sub' + args.sub + '_' + args.net, geneset_file, geneset_fmt)
    sep100.run(network_file, 'sub' + args.sub + '_' + args.net, geneset_file + '_2node_removed.gmt', 'gmt')
