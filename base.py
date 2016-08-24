__author__ = 'SungJoonPark'

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
            w.write(str(i)+"\t")
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