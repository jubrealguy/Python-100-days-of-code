def switch(length, pos, array):
    arr = array[:]

    for i in range(length):
        if i < pos:
            arr[i+1] = array[i]
        else:
            arr[i] = array[i]
    arr[0] = array[pos -1]
    return arr
print(switch(4, 3, [1,2,3,4]))
print(switch(10, 7, [1,2,3,4,5,6,7,8,9,10]))