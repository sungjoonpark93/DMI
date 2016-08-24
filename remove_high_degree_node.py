__author__ = 'SungJoonPark'
import network_base
import networkx as nx


def remove_high_degree_node(G, top_k = 1):
    top_k_node_degree_tuple_list = network_base.get_high_degree_node(G,top_k=top_k)
    to_be_reomved_node_list  = [node_degree_tuple[0] for node_degree_tuple in top_k_node_degree_tuple_list]

    G = G.copy()
    G.remove_nodes_from(to_be_reomved_node_list)
    return G



def run_remove_high_degree_node(networkfile, top_k = 3, network_type ='undirected',edge_type ='weighted' , nodelist_outputfile=None, network_outputfile=None):
    print networkfile,network_type,edge_type,top_k
    G= network_base.read_graph(networkfile,network_type=network_type,edge_type=edge_type)

    removed_node_list = [node_degree_tuple[0] for node_degree_tuple in network_base.get_high_degree_node(G,top_k)]
    G_removed_high_degree_node = remove_high_degree_node(G,top_k=top_k)

    with open(nodelist_outputfile,'w') as w:
        for node in removed_node_list:
            w.write(node)
            w.write("\n")

    nx.write_weighted_edgelist(G_removed_high_degree_node, network_outputfile ,delimiter='\t')


def run_remove_selected_nodes(networkfile, node_list = None, network_type ='undirected',edge_type ='weighted' , nodelist_outputfile=None, network_outputfile=None):
    print networkfile,network_type,edge_type,node_list
    G= network_base.read_graph(networkfile,network_type=network_type,edge_type=edge_type)

    G_removed_node = G.copy()
    G_removed_node.remove_nodes_from(node_list)

    with open(nodelist_outputfile,'w') as w:
        for node in node_list:
            w.write(node)
            w.write("\n")

    nx.write_weighted_edgelist(G_removed_node, network_outputfile ,delimiter='\t')



if __name__ =='__main__':
    networkfile = "Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1/1_ppi_anonym_v2.txt"
    nodelist_outputfile = "Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1\selected_node_removed\subchallenge1/1_ppi_6934_removed_nodelist.txt"
    network_outputfile = "Q:\DreamChallenge-Disease Module Identification\ChallengeData\subchallenge1\selected_node_removed\subchallenge1/1_ppi_6934_removed_network.txt"
    run_remove_selected_nodes(networkfile = networkfile, node_list=['6934'],network_type='directed',edge_type='weighted', nodelist_outputfile=nodelist_outputfile , network_outputfile=network_outputfile)
