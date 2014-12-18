# -*- coding: utf-8 -*-
import subprocess

def getpb_data():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    return p.communicate()[0]

def setpb_data(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.communicate(data)

print('This Script will get clipbord data(Numbers Table) and set encoded data(Tex Table).\nPress y to start')
s=raw_input()
if s != 'y':
    print('process cancelled')
    quit()
try:
    lines=getpb_data().split('\n')
    
    data=[]
    maxclm=0
    for line in lines:
        item=line.replace('\t','&')
        maxclm=max(maxclm,len(item.split('&')))
        data+=[item]
        
        for item in data:
            if len(item.split('&'))<maxclm:
                item+='&'*(maxclm-len(item.split('&')))

        outdata='\\begin{table}[h]\n\t\\begin{tabular}{'
        for i in range(0,maxclm):
            outdata+='|c'
        outdata+='|}\\hline\n'
        for item in data:
            outdata+='\t\t'+item+'\\\\ \\hline\n'
        outdata+='\t\\end{tabular}\n\\end{table}'
except:
    print('encode error')
    exit()

p=subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
p.communicate(outdata)
