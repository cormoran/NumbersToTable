#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import subprocess


def getclipboard():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    return p.communicate()[0]


def setclipboard(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.communicate(data)


def main():
    try:
        lines = getclipboard().split('\n')
        data = []
        maxclm = 0
        for line in lines:
            item = line.replace('\t', '\t&\t')
            maxclm = max(maxclm, len(item.split('&')))
            data += [item]

        for item in data:
            if len(item.split('&')) < maxclm:
                item += '&' * (maxclm - len(item.split('&')))

        outdata = '\\begin{table}[h]\n\t\\caption{Title}\n\t\\begin{center}\n\t\\begin{tabular}{'
        outdata += '|c|'

        for i in range(1, maxclm):
            outdata += '|c'

        outdata += '|}\\hline\n'

        for item in data:
            outdata += '\t\t' + item + '\t\\\\ \\hline\n'
        outdata += '\t\\end{tabular}\n\t\\end{center}\n\end{table}'
    except:
        print('encode error')
        exit()

    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.communicate(outdata)

if __name__ == '__main__':

    print('This Script will get clipbord data(Numbers Table) and set encoded data(Tex Table).\nPress y to start')
    s = raw_input()
    if s != 'y':
        print('process cancelled')
        quit()
    else:
        main()
