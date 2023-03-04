a=[2,3,4]
b=[2,3,5]
person1=person2=0
for i in range(3):
    if a[i] > b[i]:
        person1= person1+1
    elif a[i] < b[i]:
        person2=person2+1
print(person1,person2)






