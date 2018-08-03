# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:53:50 2018

@author: n10027301
"""

import matplotlib.pyplot as plt
import numpy as ny
import pandas as pd

filename=[]
title=[]
for i in range(10):
    filename.append('Method 1_0000'+str(i)+' LC.xlsx')
    title.append('b'+str(i))

print(filename, title)

data00 = pd.read_excel(filename[0])
data01 = pd.read_excel(filename[1])
data02 = pd.read_excel(filename[2])
data03 = pd.read_excel(filename[3])
data04 = pd.read_excel(filename[4])
data05 = pd.read_excel(filename[5])
data06 = pd.read_excel(filename[6])
data07 = pd.read_excel(filename[7])
data08 = pd.read_excel(filename[8])
data09 = pd.read_excel(filename[9])

fig = plt.figure(dpi=128, figsize=(15,6))

plt.subplot(1,2,1)
plt.plot(data00['Depth (nm)'], data00['Load (µN)'], 
                linewidth=3, label=title[0], color='r')
plt.plot(data01['Depth (nm)'],data01['Load (µN)'],
                linewidth=3, label=title[1], color='g')
plt.plot(data02['Depth (nm)'],data02['Load (µN)'],
                linewidth=3, label=title[2], color='b')
plt.plot(data03['Depth (nm)'],data03['Load (µN)'],
                linewidth=3, label=title[3], color='m')
plt.plot(data04['Depth (nm)'],data04['Load (µN)'],
                linewidth=3, label=title[4], color='k')

plt.title('(a)', fontsize=16, fontweight='bold', loc ='left')
plt.legend(loc='upper left', fontsize=12)
plt.xlabel(r'Depth '+'(nm)', fontsize=12)
plt.ylabel(r'Load ('+'$\mu$'+'N)', fontsize=12)
plt.tick_params(axis='both', labelsize=12, direction='in') 
x1=1500
y1=500
plt.xlim(0,x1)
plt.ylim(0,y1)
plt.xticks(ny.linspace(0,x1,x1/300+1,endpoint=True)) 
plt.yticks(ny.linspace(0,y1,y1/100+1,endpoint=True))


plt.subplot(1,2,2)
plt.plot(data05['Depth (nm)'], data05['Load (µN)'], 
                linewidth=3, label=title[5], color='r')
plt.plot(data06['Depth (nm)'],data06['Load (µN)'],
                linewidth=3, label=title[6], color='g')
plt.plot(data07['Depth (nm)'],data07['Load (µN)'],
                linewidth=3, label=title[7], color='b')
plt.plot(data08['Depth (nm)'],data08['Load (µN)'],
                linewidth=3, label=title[8], color='m')
plt.plot(data09['Depth (nm)'],data09['Load (µN)'],
                linewidth=3, label=title[9], color='k')

plt.title('(b)', fontsize=16, fontweight='bold', loc ='left')
plt.legend(loc='upper left', fontsize=12)
plt.xlabel(r'Depth '+'(nm)', fontsize=12)
plt.ylabel(r'Load ('+'$\mu$'+'N)', fontsize=12)
plt.tick_params(axis='both', labelsize=12, direction='in') 
x2=1200
y2=500
plt.xlim(0,x2)
plt.ylim(0,y2)
plt.xticks(ny.linspace(0,x2,x2/300+1,endpoint=True)) 
plt.yticks(ny.linspace(0,y2,y2/100+1,endpoint=True))

plt.show()
#plt.savefig('nano-4.jpg', bbox_inches='tight', dpi=300)
#plt.savefig('nano-5.jpg', dpi=300)