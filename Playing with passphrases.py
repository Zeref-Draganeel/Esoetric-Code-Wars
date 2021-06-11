#https://www.codewars.com/kata/559536379512a64472000053/train/python
play_pass=lambda s, n:''.join([x.lower()if p%2 else x.upper()for p,x in enumerate(s.translate(str.maketrans('abcdefghijkmlnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789','abcdefghijkmlnopqrstuvwxyz'[n:]+'abcdefghijkmlnopqrstuvwxyz'[:n]+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[n:]+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:n]+'9876543210')))])[::-1]
