#屏蔽词转换

a = input("推荐输入：'a'是第一个字母；真是运气好啊，简直是very good！对了，你好！我是MT。你是 谁？!\n选择推荐输入，请键入yes\n")
if a == 'yes':
    a = "'a'是第一个字母；真是运气好啊，简直是very good！对了，你好！我是MT。你是 谁？!"
else:
    pass
    
with open(r'C:\Users\yc\Desktop\shield.txt', 'r') as f:
    for line in f:
        str1 = line.strip()#把末尾的 \n 删掉
        if str1 in a:
            str2 = a.replace(str1, '*')
            a = str2
print("替换字：'a' '你好' 'good' '你是 谁？'\n", a)