def twoSum(list,target):
    dic={}
    for key,value in enumerate (list):
        if (target-value in dic):
            return (dic[target-value],key)
        dic[value]=key


if __name__=='__main__':
    arr=[12,1,24,25]
    target=25
    a=twoSum(arr, target)
    print(a)


