#https://www.codewars.com/kata/56f78a42f749ba513b00037f/train/python
rolldice_sum_prob=lambda a,b:len([_ for _ in [*__import__('itertools').product(range(1,7),repeat=b)]if sum(_)==a])/6**b
