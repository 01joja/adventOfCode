import os

path = os.path.dirname(os.path.abspath(__file__))
day = os.path.abspath(__file__).split("Solution")[0][-2:]
path = os.path.join(path,day+".data")

data: list[str] = []
with open(path) as f:
    for l in f:
        data.append(l.replace("\n", ""))
