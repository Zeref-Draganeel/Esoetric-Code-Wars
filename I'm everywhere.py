#https://www.codewars.com/kata/6097a9f20d32c2000d0bdb98/train/python
i=lambda _:"Invalid word" if not _ or sum(map(lambda o:_.lower().count(o),'aeiou'))>=len(_)/2 or _[0]in['I']or _[0]==_[0].lower() else 'i'+_
