#猜数字小游戏
import random
j = 0
for i in range(10000):
	a = input("这儿有一个猜数字小游戏，你愿意玩吗？愿意 yes， 任意键退出\n")
	if a == "yes":
		b = random.randint(1,100)
		for e in range(1, 6):
			c = int(input("游戏开始,请输入你的的数字（提示1-100，一局五次机会。）：\n"))
			if c > b:
				print("bigger!")
				if e == 5:
					print("本局机会用光！失败！")
			elif c < b:
				print("smaller!")
				if e == 5:
					print("本局机会用光！失败！")
			else:
				print("right!Win!\n本局游戏结束！")
				j += 1
				break			
	elif i > 0 and a !="yes":
		u = j / i
		print("bye~期待与你相见哟\n战果：\n参与局%d;\n平均猜中：%f." %(i, u))
		break
	else:
		print("bye~期待与你相见哟")
		break