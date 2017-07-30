import numpy as np
import pickle
import matplotlib.pyplot as plt
from metric import new_distance
from matplotlib.backends.backend_pdf import PdfPages

import os
Times = 20
result_new = []
result_LA = []
result_MRW = []
count = 0
#t = [0,1,2,3,4,5,6,7,8,10,11,12,13,15]
#Times = len(t)
for times in range(Times):
    count += 1
    for p_num in range(0,4):
        num = times*6+p_num
        f_new = open('.\\result\\'+str(num)+'\\opt_res_new_avg.pkl','rb')
        f_LA = open('.\\result\\'+str(num)+'\\opt_res_LA.pkl','rb')
        f_MRW = open('.\\result\\'+str(num)+'\\opt_res_MRW.pkl','rb')

        opt_new = pickle.load(f_new)

        min_dis_new = 99
        for i in range(len(opt_new)):
            if min_dis_new>opt_new[i][2]:
                min_dis_new = opt_new[i][2]
        if count == 1:
            result_new.append(min_dis_new)
        else:
            result_new[p_num] += min_dis_new

        opt_LA = pickle.load(f_LA)
        min_dis_LA = 99
        for i in range(len(opt_LA)):
            if min_dis_LA>opt_LA[i][2]:
                min_dis_LA = opt_LA[i][2]
        if count == 1:
            result_LA.append(min_dis_LA)
        else:
            result_LA[p_num] += min_dis_LA

        opt_MRW = pickle.load(f_MRW)
        min_dis_MRW = 99
        for i in range(len(opt_MRW)):
            if min_dis_MRW > opt_MRW[i][2]:
                min_dis_MRW = opt_MRW[i][2]
        if count == 1:
            result_MRW.append(min_dis_MRW)
        else:
            result_MRW[p_num] += min_dis_MRW

        f_new.close()
        f_LA.close()
        f_MRW.close()
impMRW = []
impLA = []
for p_num in range(0,4):
    result_MRW[p_num] = result_MRW[p_num]/(Times)
    result_LA[p_num] = result_LA[p_num] / (Times)
    result_new[p_num] = result_new[p_num] / (Times)
    impMRW.append(round((result_MRW[p_num]-result_new[p_num])/result_MRW[p_num]*100,2))
    impLA.append(round((result_LA[p_num]-result_new[p_num])/result_LA[p_num]*100,2))

print(impMRW)
print(impLA)

pdf = PdfPages('Facebook.pdf')
x_axis = [0.1,0.2,0.3,0.4]
print(result_LA)
print(result_new)
print(result_MRW)
plt.plot(x_axis,result_new, ls='-.', marker = 'o', label = 'TopKRank')
plt.plot(x_axis,result_LA,  ls='--',marker = 's', label = 'LA')
plt.plot(x_axis,result_MRW, ls='-', marker = '^', label = 'MRW')



#plt.arrow(0.4,result_new[3],0,result_LA[3]-result_new[3],arrowprops=dict(arrowstyle='<->'))

plt.annotate('', xy=(0.25,0.220), xytext=(0.25, 0.236),
    arrowprops=dict(arrowstyle="<->"))
plt.text(0.225, 0.228, '6%',fontsize = 15)

plt.annotate('', xy=(0.325,0.20), xytext=(0.325, 0.238),
    arrowprops=dict(arrowstyle="<->"))
plt.text(0.33, 0.22, '19%', fontsize=15)

plt.legend()
plt.xlabel('Observation Probability')
plt.ylabel('Distance from True Rankings')
plt.grid(True)
plt.title("Predicting User Interactions on Facebook")


plt.show()
#pdf.savefig()
#pdf.close()

