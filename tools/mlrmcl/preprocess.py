__author__ = 'SungJoonPark'
import pandas as pd
import os

def ChallengeData_to_MLRMCLinputfile(chanllengeData,MLRMCLinputfile,type='unweighted'):
    df = pd.read_csv(chanllengeData, sep='\t',header=None)
    node_list = set(list(df[0].values)+list(df[1].values))
    if type=='weighted':
        type_value = 1

        node_num = len(node_list)
        edge_num = len(df.index)

        #key is node and value is list that element is node, weight tuple connected with key node
        network_dict={}

        for row in df.values:
            node1=int(row[0])
            node2=int(row[1])
            edge_weight=row[2]

            if node1 not in network_dict:
                network_dict[node1]=[(node2,edge_weight)]
            elif node1 in network_dict:
                network_dict[node1].append((node2,edge_weight))

            if node2 not in network_dict:
                network_dict[node2]=[(node1,edge_weight)]
            elif node2 in network_dict:
                network_dict[node2].append((node1,edge_weight))


        w= open(MLRMCLinputfile,'w')
        w.write(str(node_num)+" "+str(edge_num)+" "+str(type_value)+"\n")
        for key in sorted(network_dict.keys()):
            for connected_node_and_weight_tuple in network_dict[key]:
                connected_node = connected_node_and_weight_tuple[0]
                edge_weight = connected_node_and_weight_tuple[1]
                w.write(str(connected_node)+" "+str(edge_weight)+" ")
            w.write("\n")
        w.close()

        return network_dict

    elif type=='unweighted':
        node_num = len(node_list)
        edge_num = len(df.index)

        #key is node and value is list that element is node, weight tuple connected with key node
        network_dict={}

        for row in df.values:
            node1=int(row[0])
            node2=int(row[1])

            if node1 not in network_dict:
                network_dict[node1]=[node2]
            elif node1 in network_dict:
                network_dict[node1].append(node2)

            if node2 not in network_dict:
                network_dict[node2]=[node1]
            elif node2 in network_dict:
                network_dict[node2].append(node1)


        w= open(MLRMCLinputfile,'w')
        w.write(str(node_num)+" "+str(edge_num)+"\n")
        max_index = max(network_dict.keys())
        for key in range(max_index+1):
            if key in network_dict:
                for connected_node in network_dict[key]:
                    w.write(str(connected_node)+" ")
            elif key not in network_dict:
                   w.write(str(0)+" ")
            w.write("\n")
        w.close()

if __name__ =='__main__':

    dataset_list = ["1_ppi_anonym_v2.txt","2_ppi_anonym_v2.txt","3_signal_anonym_directed_v3.txt_duplicates_removed.txt","4_coexpr_anonym_v2.txt",
                    "5_cancer_anonym_v2.txt","6_homology_anonym_v2.txt_normalized_0to1_top_0.150.txt"]

    input_dir = "Q:\DreamChallenge-Disease Module Identification\ChallengeData/subchallenge1/"
    inputfile_list = map(lambda x : input_dir+x, dataset_list)

    output_dir = "Q:\DreamChallenge-Disease Module Identification\Tools\MLR-MCL\mlrmcl1.2\data\subchallenge1\leaderboard_round1_3rd_submission/"
    outputfile_list = map(lambda x:output_dir + os.path.splitext(x)[0]+".graph", dataset_list)

    for i,inputfile in enumerate(inputfile_list):
        print inputfile, outputfile_list[i]
        ChallengeData_to_MLRMCLinputfile(inputfile, outputfile_list[i])