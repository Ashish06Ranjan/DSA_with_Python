"""
Problem : 1186A. Vus the Cossack and a Contest

Approach : take input and then compare the 1st input with the other input 

"""

a,b,c=map(int,input().split())

if b>=a and c>=a :
    print("Yes")
else:
    print("No")
