#https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python
persistence=lambda n,s=0:persistence(__import__('math').prod(map(int,str(n))),s+1) if n>9 else s
