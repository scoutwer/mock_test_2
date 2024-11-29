import json

def f(years,avg_grade,course):
    list = []
    count = 0
    arr = []
    with open("data.json", 'r') as file:
        students = json.load(file)
 
    for student in students:
        if student["age"] >= years:
            list.append(student)
    for i in list:
        for x in i["studies"]["courses"]:
            if x["name"] == course:
                if sum(x["grades"]) / len(x["grades"]) >= avg_grade:
                    count = count + 1
    return count
                    
                    

if __name__ == "__main__":
    print(f(21,4,"statistics"))   
 

