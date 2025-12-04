import os

path = os.path.dirname(os.path.abspath(__file__))
day = os.path.abspath(__file__).split("Solution")[0][-2:]
path = os.path.join(path,day+".data")

data: list[str] = []
with open(path) as f:
    for l in f:
        data.append(l.replace("\n", ""))

counter = 50
zeroHits = 0
for instruction in data:
    if instruction[0] == "R":
        counter += int(instruction[1:])
    else:
        counter -= int(instruction[1:])
    if counter % 100 == 0:
        zeroHits +=1

print(zeroHits)


counter = 50
zeroHits = 0
for instruction in data:
    oldCounter = counter
    if instruction[0] == "R":
        counter += int(instruction[1:])
        while counter > oldCounter:
            oldCounter +=1
            if oldCounter%100 == 0:
                zeroHits +=1
    else:
        counter -= int(instruction[1:])
        while counter < oldCounter:
            oldCounter -=1
            if oldCounter%100 == 0:
                zeroHits +=1
print(zeroHits)