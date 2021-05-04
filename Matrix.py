x = 3
y = 3
res = []
val = 0
for i in range(y):
    l = []
    for j in range(x):
       l.append(val)
       val += 1
    res.append(l)
s = []
for i in range(y):
    for j in range(x):
        s.append(str(res[i][j]))
print(s)
print(",".join(s))
print(res)
print(res[0])
print(res[1])
print(res[2])


def horizontal_and_vertical_neighbors (lst,i,j):
    result = []
    try:
        if 0 <= i-1 <= len(lst):# Верхний элемент
            result.append(str(lst[i - 1][j]))
        else:
            result.append(str(None))
    except:
        result.append(str(None))
    try:
        if 0 <= j+1 <= len(lst[i]): # Правый элемент
            result.append(str(lst[i][j+1]))
        else:
            result.append(str(None))
    except:
        result.append(str(None))
    try:
        if 0 <= i + 1 <= len(lst):  # Нижний элемент
            result.append(str(lst[i + 1][j]))
        else:
            result.append(str(None))
    except:
        result.append(str(None))
    try:
        if 0 <= j - 1 <= len(lst[i]):  # Правый элемент
            result.append(str(lst[i][j - 1]))
        else:
            result.append(str(None))
    except:
        result.append(str(None))
    return result
print(",".join(horizontal_and_vertical_neighbors(res,-1,1)))