import os
import random
train=[]
dev=[]
test=[]
with open("train.triples","r",encoding="utf8") as f:
    for line in f:
        e1, e2, r = line.strip().split()
        train.append((e1,e2,r))
with open("dev.triples","r",encoding="utf8") as f:
    for line in f:
        e1, e2, r = line.strip().split()
        dev.append((e1,e2,r))
with open("test.triples","r",encoding="utf8") as f:
    for line in f:
        e1, e2, r = line.strip().split()
        test.append((e1,e2,r))
all = train + dev + test
length = len(all)
random.shuffle(all)
train_pro = int(0.7*length)
dev_pro = int(0.2*length)
f_train = open("train_new.triples","w",encoding="utf8")
f_dev = open("dev_new.triples","w",encoding="utf8")
f_test = open("test_new.triples","w",encoding="utf8")
f_all = open("all_new.triples","w",encoding="utf8")
for i in range(len(all)):
    item=all[i]
    f_all.write(" ".join([item[0],item[1],item[2]]))
    f_all.write("\n")
    if i > train_pro+dev_pro:
        f_test.write(" ".join([item[0],item[1],item[2]]))
        f_test.write("\n")
    elif i > train_pro:
        f_dev.write(" ".join([item[0],item[1],item[2]]))
        f_dev.write("\n")
    else:
        f_train.write(" ".join([item[0],item[1],item[2]]))
        f_train.write("\n")