

code=0
times = 2
answer = 666
while code != answer and times >= 0:
    code = input("please enter the code:")
    if "*" in code:
        continue
    else:
        if times > 0:
            print ("try again")
            times -= 1
        else:
            print ("sorry, you have no chance")
            break

print("THX")
