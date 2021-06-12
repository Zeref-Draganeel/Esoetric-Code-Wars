#https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
spin_words=lambda _:' '.join([x[::-1]if len(x)>4else x for x in _.split()])
