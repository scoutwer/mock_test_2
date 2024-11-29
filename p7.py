def f(arr):
    for i in arr: 
        res = False
        if len(i) > 12 or len(i) < 4:
            arr.remove(i)
            continue
        if i.islower() == False:
            arr.remove(i)
            continue
        if "_" not in i:
            arr.remove(i)
            continue
        for x in i:
            if x.isdigit() == True:
                res = True
        if res == False:
            arr.remove(i)
    return len(arr)
        
    



print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))