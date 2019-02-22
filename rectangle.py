import random

def rectangle(w=5, l=5, i="*"):
    for wide in range(w):
        for leng in range(l):
            if leng < l-1:
                print(i, end='')
            else:
                print(i)
rectangle(4,5, "#")
rectangle(4,9, "#")
rectangle(8,3)