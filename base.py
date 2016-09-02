__author__ = 'SungJoonPark'

def write_edgelist(edge_list, output_filename):
    w= open(output_filename,'w')
    for edge in edge_list:
        w.write(edge[0]+"\t"+edge[1]+"\t"+str(edge[2])+"\n")
    w.close()

def read_genesetfile(genesetfile=None,input_format="txt"):
    geneset_list = []
    with open(genesetfile,'r') as r:
        for line in r:
            if input_format =='txt':
                #Node label should be string not integer even is integer!
                geneset_list.append(line.strip().split("\t"))
            elif input_format =='gmt':
                #Node label should be string not integer even is integer!
                geneset_list.append(line.strip().split("\t")[2:])
    geneset_list = [gene_list for gene_list in geneset_list]
    return geneset_list


def write_genesetfile(geneset_list, outputfile=None, output_format ='challenge'):
    w=open(outputfile,'w')
    for i,geneset in enumerate(geneset_list):
        if output_format=='challenge':
            w.write(str(i+1)+"\t")
            w.write("0.5"+"\t")
            w.write("\t".join(geneset))
            w.write("\n")
        elif output_format=='txt':
            w.write("\t".join(geneset))
            w.write("\n")
        elif output_format=='gmt':
            w.write(str(i)+"\t")
            w.write("TEMP_DESCIPTION"+"\t")
            w.write("\t".join(geneset))
            w.write("\n")
    w.close()



def convert_genesetfile_format(input_genestfile=None, input_format='gmt', outputfile=None, output_format='challenge'):
    geneset_list = read_genesetfile(genesetfile=input_genestfile,input_format=input_format)
    write_genesetfile(geneset_list, outputfile=outputfile , output_format=output_format)