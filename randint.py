#使用random.randint()方法，推测
import math
a = pow(52,8)
b = pow(52,8)
c = 1
for i in range(1,200):
    d = (a-i)
    c = d / b
    c *= c  
    #print("每一次::", str(c))
print("全不相同的概率：%.30f" %c)
#print(c)