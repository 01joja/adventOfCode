import os

path = os.path.dirname(os.path.abspath(__file__))
day = os.path.abspath(__file__).split("Solution")[0][-2:]
path = os.path.join(path,day+".data")

data: list[str] = []
with open(path) as f:
    for l in f:
        data.append(l.replace("\n", ""))

#data = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]

counter = 0
for d in data:
    max1 = 0
    index = 0
    for i in range(len(d)-1): 
        if int(d[i])>max1:
            index = i
            max1 = int(d[i])
            if max1 == 9:
                break 
    max2 = 0
    d = d[index+1:]
    for i in range(len(d)):
        if int(d[i])>max2:
            index = i
            max2 = int(d[i])
            if max2 == 9:
                break 
    counter += max1*10+max2

print(counter)

def greedy(list,start,end):
    maxInt = 0
    index = 0
    d = list[start:]
    for i in range(len(d)-end): 
        if int(d[i])>maxInt:
            index = i
            maxInt = int(d[i])
            if maxInt == 9:
                break 
    return (maxInt,start+index+1)

counter = 0
for d in data:
    max = 0
    index = 0
    
    for i in range(12):
        (maxInt,index) = greedy(d,index,11-i)
        max = max*10+maxInt
    #print(max)
    counter += max

print(counter)