__author__ = "WonhoShin"

import os
from subprocess import check_call

rootdir = "./"
network_list = [
    #["data/1_ppi_anonym_v2.txt_bin.txt", "output/1_ppi_anonym"],
    #["data/2_ppi_anonym_v2.txt_bin.txt","output/2_ppi_anonym.output"],
    #["data/3_signal_anonym_directed_v3.txt_duplicates_removed.txt_bin.txt", "output/3_signal_anonym_directed"]
    #["data/4_coexpr_anonym_v2.txt_bin.txt", "output/4_coexpr_anonym.output"],
    #["data/5_cancer_anonym_v2.txt_bin.txt", "output/5_cancer_anonym.output"],
    #["data/6_homology_anonym_v2.txt_bin.txt", "output/6_homology_anonym"]
    #["data/whole_network_conf_keep_highest.txt_bin.txt", "output/whole_network_conf_keep_highest"]
]

exe_file = rootdir + "scanpp"
_tmp = rootdir + "tmp"

for _f in network_list:
    for _e in [x*0.05 for x in range(20)]:
        for _m in range(1,11):
            print _f[0], _e, _m
            epsilon = str(_e)
            mu = str(_m)

            fin = rootdir + _f[0]
            _fout = rootdir + _f[1] + '_e_' + epsilon + '_m_' + mu + '.gmt'
            fout = open(_tmp , "w")

            # run scan++ and get result as tmp file
            check_call([exe_file, '-e', epsilon, '-m', mu, '-r', fin], stdout=fout)
            fout.close()

            # parse scan++ result
            _res = {}
            ftmp = open(_tmp, "r")
            ftmp.readline()

            while True:
                line = ftmp.readline()
                if not line:
                    break
                if line.split("\t")[1] not in _res:
                    _res[line.split("\t")[1]] = []
                _res[line.split("\t")[1]].append(line.split("\t")[0])
            ftmp.close()

            # print parsed data in rootdir/output/
            fout = open(_fout, "w")
            i = 1
            for key in _res:
                if len(_res[key]) == 1:
                    continue
                fout.write(str(i) + "\t" + _f[0] + "\t"+ "\t".join(_res[key]) + "\n")
                i += 1
            fout.close()
            os.remove(_tmp)
