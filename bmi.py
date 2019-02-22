#BMI指数
a = input("这儿有一个BMI测试，你愿意做吗？愿意 yes\n")
if a == "yes":
	b = input("这是一个BMI测试:\n您的数据将不会被储存，请放心输入\n 请输入你的体重（kg）:\n")
	c = input("接下请输入你的身高（m）:\n")
	bmi = float(b) / float(c)/float(c)
	if bmi < 18.5:
		print("体重偏轻\n感谢您的使用")
	elif bmi >= 24:
		print("体重偏轻\n感谢您的使用")
	else:
		print("体重正常\n感谢您的使用")

else:
	print("bye~期待与你相见哟")