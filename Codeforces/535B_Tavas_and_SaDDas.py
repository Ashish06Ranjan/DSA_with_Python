"""
Problem : 535B. Tavas and SaDDas

"""
n = input()
 
length = len(n)
 
before = (2 ** length) - 2
 
pos = 0
 
for ch in n:
    pos *= 2
    if ch == '7':
        pos += 1
 
print(before + pos + 1)
