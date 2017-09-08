
## 1. 视频中我们说 sum() 这个BIF有个缺陷，就是如果参数里有字符串类型的话就会报错，请写出一个新的实现过程，自动“无视”参数里的字符串并返回正确的计算结果
name = input("请输入待查找的用户名：")
score=[["小甲鱼","80"],["sally", "90"],["joe","88"],["hah","78"],["emily","98"]]
isfind = False

for each in score:
    if name in each:
        print(name , score[1])
        isfind = True
        break
if isfind == False:
    print("cannot find")