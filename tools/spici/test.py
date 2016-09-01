import os
temp = ["../abc/abdf/abc.txt","../abc/abdf/abc_Dfd.txt"]
parameter = "_default.txt"
print map(lambda x:os.path.splitext(x)[0]+parameter, temp)