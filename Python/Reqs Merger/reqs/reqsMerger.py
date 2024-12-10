import os

fileName = __file__
if type(fileName.split("\\")) == list and len(fileName.split("\\"))>1:
    fileName = fileName.split("\\")[-1]
    filePath = __file__.replace(fileName,"")
else:
    fileName = fileName.split("/")[-1]
    filePath = __file__.replace(fileName,"")
os.chdir(filePath)

hyperMerge = []
uniqueMerge = []
dirConts = list(os.listdir())
dirConts.remove("reqsMerger.py")
dirConts = [x for x in dirConts if not x == ".DS_Store"]
for i in dirConts:
    with open(i) as f:
        for j in f.readlines():
            hyperMerge.append(j)

[uniqueMerge.append(val) for val in hyperMerge if val not in uniqueMerge and val != []]

with open("requirements.txt","w") as f:
    f.write("")

for i in uniqueMerge:
    with open("requirements.txt","a") as f:
        f.write(i)
print("done")