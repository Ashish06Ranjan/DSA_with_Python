"""
Problem : 71A. A. Way Too Long Words
Approach : Take each word as input. Check its length.
            If the length is more than 10: 
            Take the first letter.
            Count the letters between the first and last letters (length - 2).
            Take the last letter.
            Combine them. Otherwise, print the word as it is.

"""

n=int(input())
for _ in range(n):
    a=input()
    if len(a)>10:
        print(a[0]+str(len(a)-2)+a[-1])
    else:
        print(a)
