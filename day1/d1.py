with open('inp.txt','r') as f:
    inp = f.read().strip().split('\n\n')

rlist = []
for i in inp:
    v = i.split("\n")
    rlist.append(sum(map(int,v)))

part_one = max(rlist)

part_two = sum(sorted(rlist)[-3:])

print(part_one)
print(part_two)