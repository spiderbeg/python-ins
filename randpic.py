import random

a1 = 0
a2 = 0
a3 = 0
for i in range(1000):
	a = random.randint(1,3)
	if a == 1:
		a1 += 1
	if a == 2:
		a2 += 1	
	if a == 1:
		a3 += 1
a = a1 + a2 + a3
b1 = a1 / a
b2 = a2 / a
b3 = a3 / a
print(b1, b2, b3)