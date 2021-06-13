#https://www.codewars.com/kata/598c1bc6a04cd3b8dd000012/train/python
restaurant=lambda a,e,i:(lambda a=[a],e=[e],d=[0],s=[0]:[[(a.__setitem__(0,a[0]-1)if a[0]else[s.__setitem__(0,s[0]+1)if s[0]<e[0]else[s.__setitem__(0,s[0]-1),e.__setitem__(0, e[0]-1)]if e[0]else d.__setitem__(0,d[0]+1)])if v==1else e.__setitem__(0,e[0]-1)if e[0]>s[0]else d.__setitem__(0,d[0]+2)for v in i],d[0]][1])()
