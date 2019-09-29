list1 = [1, 2, 3]
list2 = [6, 7, 8]
list3 = [11, 12, 13]
list_sum = list1 + list2 + list3
a = len(list1)
b = len(list2)
c = len(list3)
print(list_sum)
e = []
f = []
g = []
for i in range(a):
    e += [list_sum[i]]
print(e)
for j in range(b):
    f.append(list_sum[j+3])
print(f)
for k in range(c):
    g.append(list_sum[k+6])
print(g)


    
