a = [[1,2,3],[4,5,6],[7,8,9]]
sums = []
for i in range(len(a)):
    temp =0
    for j in a:
        temp = temp + j[i]
    sums.append(temp)

print("sums ",sums)