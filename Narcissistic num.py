def Narcissistic(): #153=1**3 + 5**3 +3**3
    for each in range(100, 1000):
        sum = 0
        temp = each
        while temp:
            sum = sum + (temp % 10) ** 3
            temp = temp // 10
        if sum == each:
            print(each)
print(Narcissistic())