def f(arr):
    dic = {"value": arr[0][0],
           "row":0,
           "column": 0 
           }
    for i in range(len(arr)):
        for x in range(len(arr[i])):
            if arr[i][x] < dic["value"]:
                dic["value"] = arr[i][x]
                dic["row"] = i
                dic["column"] = x
    if dic["row"] == dic["column"]:
        return True
    else:
        return False
    
if __name__ == "__main__" :
    print(f([[7,8],[5,3],[9,4]]))
    print(f([[7,8,5,3],[9,4,2,6]]))