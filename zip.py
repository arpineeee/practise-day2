def zip(data1, data2):
        lst = [None] * len(data1)
        for i in range(len(data1)):
             lst[i] = [data1[i], data2[i]]
        
        return lst

data1 = [21, 13, 7, 33]
data2 = [95, 48, 123, 77]
print(zip(data1, data2))
