def f(arr):
    diffrent = {}
    for i in arr:
        if i not in diffrent.keys():
            diffrent[i] = 1 
        else:
            diffrent[i] += 1 
    for i in diffrent:
        if diffrent[i] == 1:
            return i

if __name__ == "__main__":
    print(f([7,7,7,7,7,5,7,7]))
    print(f(["a","a","b"]))

