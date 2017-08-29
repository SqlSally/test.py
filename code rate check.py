# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位


#  中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位



# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位


special = r'''!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
number = "0123456789"
alpha = "aabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

code = input("please enter your code:")
length = len(code)

while code.isspace() == True or length == 0:
    code = input("Please enter again: ")

if length<=8 :
    flag_len=1
elif 8<length<=16:
    flag_len = 2
else:
    flag_len = 3
flag_con = 0

for each in code:
    if each in special:
        flag_con += 1
        break

for each in code:
    if each in number:
        flag_con += 1
        break

for each in code:
    if each in alpha:
        flag_con += 1
        break

while True:
    print("您的密码定义为： ", end="")
    if flag_con == 1 or flag_len ==1:
        print("简单")
    elif flag_con ==2 or flag_len ==2:
        print("中等")
    else:
        print("困难")
        print("great")
        break
    print("请按以下方式提升您的密码安全级别：\n\
        \t1. 密码必须由数字、字母及特殊字符三种组合\n\
        \t2. 密码只能由字母开头\n\
        \t3. 密码长度不能低于16位")
    break









