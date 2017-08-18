import random
secret= random.randint(1, 10)
times=3
guess=0
while guess != secret and times>0:
    temp = input("number:")
    if  temp.isdigit():
        guess = int(temp)
        times = times - 1
        if guess == secret:
            print("great", end=" ")
            break
        elif guess>secret:
            print("大了", end=" ")
        else:
            print("小了")
        if times>0:
            print("再试一次", end=" ")
        else:
            print("机会用完了", end=" ")
    else:
        print("重新输入：")
print("game over")

