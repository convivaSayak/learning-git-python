grades=[78,58,28,38,14,42]
min_grade=38
n=len(grades)
result=[]
for i in range (n):
    if i >=38:
        mod= i%5
        if (5-mod) <3:
            i=i+(5-mod)
            result.append(i)
print(result)
