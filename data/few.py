import pandas as pd
import numpy as np
#main
if __name__ == '__main__':
    rootpath= 'FB15K-237'
    #read data
    df = pd.read_table(rootpath+'/train.triples', sep='\t', header=None)
    #read two columns
    df = df[[2]]
    #统计df中的每个元素出现的次数
    df = df.stack().value_counts()
    #统计后10%的元素
    df = df[df < df.quantile(0.15)]
    #转换为list
    df = df.index.tolist()
    with open (rootpath+'/few_shot.txt', 'w') as f:
        #输出df中的元素
        f.write('\n'.join(df))

