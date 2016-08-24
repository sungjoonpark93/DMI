__author__ = 'SungJoonPark'
def sub1_of_geneid_from_cossyresult_and_make_for_txtformat(cossy_reulst_gmt_flie):

    result_list =[]
    with open(cossy_reulst_gmt_flie) as r:
        for line in r:
            line_list = line.strip().split("\t")[2:]
            if "NA" in line_list:
                line_list.remove('NA')
            line_list=map(lambda x:int(x)-1,line_list)
            result_list.append(line_list)

    w = open(cossy_reulst_gmt_flie,'w')
    for line in result_list:
        line = map(lambda x:str(x),line)
        w.write("\t".join(line))
        w.write("\n")


if __name__ =='__main__':
    # sub1_of_geneid_from_cossyresult_and_make_for_txtformat("./1_1_ppi.gmt")
    sub1_of_geneid_from_cossyresult_and_make_for_txtformat("./1_2_ppi.gmt")
    # sub1_of_geneid_from_cossyresult_and_make_for_txtformat("./1_3_signal.gmt")
    # sub1_of_geneid_from_cossyresult_and_make_for_txtformat("./1_4_coexpr.gmt")
    # sub1_of_geneid_from_cossyresult_and_make_for_txtformat("./1_5_cancer.gmt")
    #sub1_of_geneid_from_cossyresult_and_make_for_txtformat("./1_6_homology.gmt")
    pass