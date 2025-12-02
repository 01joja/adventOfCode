import os

path = os.path.dirname(os.path.abspath(__file__))
day = os.path.abspath(__file__).split("solution")[0][-2:]
path = os.path.join(path,day+".data")

data: list[str] = []
with open(path) as f:
    for l in f:
        data.append(l.replace("\n", ""))

area = 0
ribbon = 0
for box in data:
    d = box.split("x")
    d[0]=int(d[0])
    d[1]=int(d[1])
    d[2]=int(d[2])
    sides = []
    sides.append(d[0]*d[1])
    sides.append(d[0]*d[2])
    sides.append(d[1]*d[2])
    smallest = sides[0]
    for side in sides:
        area += side*2
        if smallest > side:
            smallest = side
    area += smallest
    ribbonSides = []
    ribbon += d[0]*d[1]*d[2]
    ribbonSides.append(d[0]+d[0])
    ribbonSides.append(d[1]+d[1])
    ribbonSides.append(d[2]+d[2])
    largest = ribbonSides[0]
    for rs in ribbonSides:
        ribbon += rs
        if rs > largest:
            largest = rs
    ribbon -= largest

print(ribbon)
print(area)