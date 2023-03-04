stack = []


def push():
    data = eval(input("enter the num->>> "))
    stack.append(data)
    print(stack)


def pop_item():
    if stack:
        item = stack.pop()
        print("removed from stack :", item)
        print(stack)
    else:
        print("i think stack is empty")


while True:
    print(" press 1 for push, 2 for pop , 3 for stop the operation")
    choice = int(input("enter your choise->>"))
    if choice==1:
        push()
    elif choice==2:
        pop_item()
    elif choice==3:
        break

    else:
        print("you are doing some thing wrong ")

