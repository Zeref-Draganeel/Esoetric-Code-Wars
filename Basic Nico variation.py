#https://www.codewars.com/kata/5968bb83c307f0bb86000015/train/python
nico=lambda k,m,p=0:(lambda f={x:[]for x in k}:[[f[k[p%len(k)]].append(i)for p,i in enumerate(m)],[[f[k[j]].append(' ')for j in range((p+1)%len(k),len(k))]if(p+1)%len(k)else None],''.join(sum(zip(*[f[x]for x in sorted(f)]),()))][-1])()
