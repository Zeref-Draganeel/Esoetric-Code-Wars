#https://www.codewars.com/kata/5b6ee22ac5cc71833f0010d7/train/python
kaprekar_split=lambda _:0 if _**2==_ else{x==_:p for p,x in enumerate((lambda k:[int(k[:i])+int(k[i:])for i in range(1,len(k))])(str(_**2)))}.get(True,-2)+1
