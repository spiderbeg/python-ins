#读取指定文件夹中文件名称及内容
#读取指定文件夹中文件名称及内容
import os
def findfile(start, name):
    list1 = []
    list2 = []
    for relpath, dirs, files in os.walk(start):
        #print(dirs)
        for j in files:
            if name in j:
                #print(j)
                list1 += [j]
            elif '.txt' in j:
                #print(j)
                with open(relpath + "\\" + j, 'r') as f: #文件路径名
                    for line in f:
                        if name in line:
                            #print(j)
                            list2 += [j]
                            break
    
    return print("含有%s关键字的文件：\n" % name, list1 + list2)
if __name__ == '__main__':
    '''dir1 = r'E:\CS\CS_Books\excel'
    namelist = ['Excel', 'sql']
    for i in namelist:
        findfile(dir1, i)'''
    dir1 = input("(推荐路径：  E:\CS\CS_Books\excel  输入路径：\n") #自己电脑的路径
    keyword = input('推荐关键字：  Excel  ;请输入关键字\n')
    findfile(dir1, keyword)    