import random
from collections import Counter
list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','i','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
list5 = []
for i in range(200):
    list4 = []
    for b in range(8):
        a = random.randint(0,51)
        list3 = [list1[a]]
        #list3 = c.split()
        #print(list3)
        list4 = list4 + list3
        #print(list4)
    str1 = ''.join(list4)
    list7 = [str1]
    #print(list7)
    list5 = list5 + list7
    #print(list5)
    for i in Counter(list5).values():
        if i > 1:
            print("same")
            c = True
        else:
            c = False
            pass
if c:
    print("有重复，请重新生成")
else:
    print("请放心使用！\n", list5)

import sys
print(sys.stdout.encoding)