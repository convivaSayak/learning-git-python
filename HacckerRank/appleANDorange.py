def countApplesAndOranges(s, t, a, b, apples, oranges):
    ta=tb=0
    for i in range(len(apples)):
        if (a+apples[i]) >= s and (a+apples[i]) <=t:
            ta=ta+1
    for i in range(len(oranges)):
        if (b + oranges[i]) >= s and (b + oranges[i]) <= t:
            tb=tb+1
    print(ta,tb)

    

