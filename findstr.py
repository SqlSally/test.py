#2. 编写一个函数 findstr（），该行书统计一个长度为2的子字符串在另一个字符串中出现的次数。
#例如：嘉定输入的字符串为
# "you cannot improve your past, buy you can improve your
# future. Once time is wasted, life is wasted."
#子字符串为“im”， 函数执行后打印“子字母穿在目标字符串中出现了3次。”

#a:  usestr
#b:  detaistr
def findstr(destr, substr):
    length = len(destr)
    count = 0
    if substr in destr:
        for each in range(length - 1):
            if destr[each] == substr[0]:
                if destr[each+1] == substr[1]:
                    count += 1
        return count

    else:
        print("no")
print(findstr("imimim", "im"))
