while True:
    temp = input("number：")
    if  temp.isdigit():
        if int(temp) % 4 == 0:
            print("闰年")
        else:
            print("非闰年")
        break
    else:
        print("gain please")
print("game over")