import os

path = os.path.dirname(os.path.abspath(__file__))
day = os.path.abspath(__file__).split("Solution")[0][-2:]
path = os.path.join(path,day+".data")

data: list[str] = []
with open(path) as f:
    for l in f:
        data.append(l.replace("\n", ""))

data = [
"..@@.@@@@.",
"@@@.@.@.@@",
"@@@@@.@.@@",
"@.@@@@..@.",
"@@.@@@@.@@",
".@@@@@@@.@",
".@.@.@.@@@",
"@.@@@.@@@@",
".@@@@@@@@.",
"@.@.@@@.@."
]

papers:list[list[int]] = [[0]*(len(data[0])+2)]*(len(data)+2)

for l in range(1,len(data)+1):
    for i in range(1,len(data[l-1])+1):
        if data[l-1][i-1] == "@":
            papers[l-1][i-1] += 1
            papers[l][i-1] += 1
            papers[l+1][i-1] += 1
            papers[l-1][i] += 1
            papers[l+1][i] += 1
            papers[l-1][i+1] += 1
            papers[l][i+1] += 1
            papers[l+1][i+1] += 1
    for p in papers:
        print(p)