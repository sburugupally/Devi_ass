import json
s="commit"
s1=""
l1=[]
l2=[]
l=[]
with open("g_log.txt","r") as fr:
    buf=fr.readlines()
print(buf)
for line in buf:
    if s in line:
        l1.append(line)
    else:
        l2.append(line)
for i in range(len(l2)):
    for line in range(0,4):
        s1+=l2[line]
    l.append(s1)
z=zip(l1,l)
d=dict(z)
print(d)
with open("j_log.json","w") as fw:
    json.dump(d,fw,indent=1)
    

