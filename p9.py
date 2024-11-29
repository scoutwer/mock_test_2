import csv

def f(value):
    arr = []
    with open("data.csv",'r') as file:
        content = csv.reader(file)
        for row in content:
            try:
                if int(row[9]) >= value:
                    arr.append(row[9])
            except:
                continue
    return len(arr)
    

print(f(9200))
print(f(11640))
            