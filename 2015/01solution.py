import os

path = os.path.dirname(os.path.abspath(__file__))
day = os.path.abspath(__file__).split("solution")[0][-2:]
path = os.path.join(path,day+".data")

with open(path) as f:
    data = f.read()

counter=0
floor=0
basement=False
for d in data:
    if not basement:
        counter+=1
    if d == "(":
        floor+=1
    else:
        floor-=1
    if floor<0:
        basement = True
print(floor)
print(counter)