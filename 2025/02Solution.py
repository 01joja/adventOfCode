import os

path = os.path.dirname(os.path.abspath(__file__))
day = os.path.abspath(__file__).split("Solution")[0][-2:]
path = os.path.join(path,day+".data")

data: list[str] = []
with open(path) as f:
    for l in f:
        data.append(l.replace("\n", ""))

#data: list[str] = ["11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"]
#data = ["11-22,38593856-38593862"]
data = data[0].split(",") 
print(data)

counter = 0
# part 1
#for d in data:
#    d = d.split("-")
#    for id in range(int(d[0]),int(d[1])+1):
#        if len(str(id))%2 == 0:
#            p1 = int(str(id)[:int(len(str(id))/2)])
#            p2 = int(str(id)[int(len(str(id))/2):])
#            if p1 == p2:
#                counter += id

counter = 0
longestID = 0
# part 2
for d in data:
    d = d.split("-")
    for id in range(int(d[0]),int(d[1])+1):
        #print(id)
        id = str(id)
        maxLength = len(id)/2
        repeatLength = 1
        while repeatLength <= maxLength:
            if len(id) % repeatLength == 0:
                isFake = True
                compare = int(id[0:repeatLength])
                #print("id:" + id)
                for i in range(repeatLength,len(id),repeatLength):
                    #print(id[i:i+repeatLength])
                    if compare != int(id[i:i+repeatLength]):
                        isFake = False
                        break
                if isFake:
                    print(True)
                    print(id)
                    counter += int(id)
                    break
            repeatLength+=1


print("counter")
print(counter)
