def f(subjects):
    dic = {}
    for key in subjects:
        dic[key] = sum(subjects[key]) / len(subjects[key])
    maximum = max(dic.values())
    for keys in dic:
        if dic[keys] == maximum:
            return keys


if __name__ == "__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))
