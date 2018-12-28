import pandas as pd
import numpy as np
import time
data = pd.DataFrame([1,2,3,4,5,'123\r\n123'])
data = data.T
# start = time.time()
# data.to_csv('test.csv',mode='a',index = False,header = False)
# data.to_csv('test.csv',mode='a',index = False,header = False)
# data.to_csv('test.csv',mode='a',index = False,header = False)
# print(time.time()-start)
import xlwt

import csv

with open('test.csv','a') as f:
    data.to_csv(f, mode='a', index=False, header=False,line_terminator = '')

