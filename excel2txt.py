#!/usr/bin/env python
#-*- coding:utf-8 -*-
import xlrd

source_path = 'C:/Users/xingbo.liu/Desktop/zancun/input.xlsx'
target_path = 'C:/Users/xingbo.liu/Desktop/zancun/output.txt'

data = xlrd.open_workbook(source_path)
table = data.sheet_by_name('aaa')
print table.nrows#行数
print table.ncols#列数 

n=i=0    
file=open(target_path,"w")  
for n in range(table.nrows):  
    for i in range(table.ncols):  
        text=table.cell_value(n,i).encode('utf-8')  
        file.write(text)   
        file.write('\n')  
file.close()       
