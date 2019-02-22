for o in range(1, 5):
	for s in range(1, 5):
		if o != s:
			for t in range(1, 5):
				if t != o and t != s:
					print(str(o) + str(s) + str(t)) 
