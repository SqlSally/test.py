### 1. 编写一个程序，求 100~999 之间的所有水仙花数。
#如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
# 例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花
import random
x = random.randint(0, 9)
y = random.randint(0, 9)
z = random.randint(0, 9)
a= x + 10 * y + 100 * z
for a in range (100, 999):
    a == x**3 + y**3 + z**3
    print (a)
