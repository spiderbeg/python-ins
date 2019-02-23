#斗地主
import random
list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','i','o','p','q','r','s',
         't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L',
         'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','big','small']
#print(list1)
random.shuffle(list1)#打乱元素
for d in range(5):
	choice = random.choice(list1)
	if choice in list1[49:50]:
		choice = random.choice(list1)
	else:
		break
print("地主牌：\n",choice)
#print(list1)
list2 = []
list3 = []
list4 = []
list5 = []
for i in list1[:17]:
    list2 = [i] + list2
for a in list1[17:34]:
    list3 = [a] + list3
for b in list1[34:51]:
    list4 = [b] + list4
for c in list1[51:54]: 
    list5 = [c] + list5
if choice in list2:
	print("第一个人优先叫地主")
if choice in list3:
	print("第二个人优先叫地主")
if choice in list4:
	print("第三个人优先叫地主")

print("第一个人：\n",list2)
print("第二个人：\n",list3)
print("第三个人：\n",list4)
print("底牌：\n",list5)