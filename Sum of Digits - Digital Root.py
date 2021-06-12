#https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
digital_root=lambda _:(lambda o=[sum(map(int,str(_)))]:[[*iter(lambda:False if len(str(o[0]))==1else o.__setitem__(0,sum(map(int,str(o[0])))),False)],o[0]][1])()
