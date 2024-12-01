def f(expression):
    expression = expression.split()
    stack = []
    for i in expression:
        if i.isdigit():
            stack.append(int(i))
        elif i in "+-":
            a = stack.pop()
            b = stack.pop()
            if i == "+":    
                stack.append(a + b)
            elif i == '-':
                stack.append(b - a)      
        else:
            raise ValueError(f"invalid token")
    return stack.pop()

if __name__ == "__main__":
    print(f("2 3 +"))
    print(f("2 6 + 4 5 - +"))
    print(f("11 7 + 15 - 14 +"))
