#奖牌榜类实现
#编程实例
import time
import random

class Medal:
    def __init__(self, country="World's Rank", goldn=0, agn=0, cun=0):
        '''默认属性'''
        self.country = country
        print('This is country: ', self.country)
        self.gold = goldn
        self.ag = agn
        self.cu = cun
    
    def add(self, numg=0, numa=0, numc=0):
        """奖牌新增"""
        self.gold += numg
        print("add gold: ", numg)
        self.ag += numa
        self.cu += numc
        print("add ag: ", numa)
        print("add cu: ", numc)

    def status(self):
        """实时信息"""
        #print('实时信息：\n gold: %d \n ag: %d \n cu: %d '  %(self.gold, self.ag, self.cu))
        return self.gold
        
    def wholen(self):
        """总和"""
        #print("whole medals:%d\n" %(self.gold + self.ag + self.cu))
        return self.gold + self.ag + self.cu

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)
list1 = ['中国','美国','韩国','日本','越南','玻利维亚','俄罗斯','朝鲜','英国','法国']
list2 = ['w','x','y','z','q','e','j','r','t','p'] #可将list换为子典
dict1 = {}
dict2 = {}
for i in range(10):
    a = random.randint(1,10)
    b = random.randint(1,20)
    c = random.randint(1,30)
    
    if i == 0:
    	list2[i] = Medal(country=list1[i],goldn=1000,agn=1000,cun=1000)
    	dict1[list1[i]] = list2[i].wholen() #奖牌总数
    	dict2[list1[i]] = list2[i].status() #金牌总数  
    else:
	    #print(list2[i])
	    list2[i] = Medal(country=list1[i],goldn=a,agn=b,cun=c)
	    #list2[i].status()
	    #list2[i].wholen()
	    dict1[list1[i]] = list2[i].wholen() #奖牌总数
	    dict2[list1[i]] = list2[i].status() #金牌总数
'''
w = Medal(country='gog0',goldn=5,agn=4,cun=3)
print(w.gold)
'''
#print(dict1)
print('各国奖牌总数排名：\n',sorted(dict1.items(), key = lambda x: x[1], reverse=True))#总数排序
print('各国金牌数排行榜：\n',sorted(dict2.items(), key = lambda x: x[1], reverse=True))#金牌排序
print('中国第一！')