#https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
likes=lambda _:((f'{_[0]}'+((f' and {_[1]}'if len(_)==2else f', {_[1]} and {_[2]}'if len(_)==3else f', {_[1]} and {len(_)-2} others')if len(_)>1 else ''))if _ else 'no one')+f" like{'s'*(len(_)<2)} this"
