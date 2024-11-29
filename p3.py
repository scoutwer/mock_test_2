def f(arr):
    rows = []
    dic = {}
    result = True
    for i in arr:
        rows.append(sum(i))
        for j in range(len(i)):
            if j not in dic.keys():
                dic[j] = i[j]
            else:
                dic[j] = dic[j] + i[j]
    for x in range(3):
        if dic[x] != rows[x]:
            result= False
        else:
            continue
    return result
        

if __name__ == "__main__":
    print(f([[3,7,2],[4,2,5],[5,2,1]]))
    print(f([[3,7,2],[4,2,5],[9,2,1]]))