def f(player1,player2):
    value_1 = 0
    value_2 = 0 
    for i in range(len(player1)):
        if player1[i] in ["A","K","J","T", "Q"]:
            value_1 += 10 
        else:
            try: 
                value_1 += int(player1[i])
                
            except:
                continue
    for j in range(len(player2)):
        if player2[j] in ["A","K","J","T", "Q"]:
            value_2 += 10 
        else:
            try: 
                value_2 += int(player2[j])
            except:
                continue
    if value_1 > value_2:
        return True
    else: 
        return False

if __name__ == "__main__":
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))



