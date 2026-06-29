"""
Problem : 151A. Soft Drinking
Approach :  Find how many toasts can be made from the drink.
            Find how many toasts can be made from lime slices.
            Find how many toasts can be made from salt.
            The limiting resource is the minimum of these three.
            Divide by the number of friends to get the number of toasts per friend.
"""

n, k, l, c, d, p, nl, np = map(int,input().split())

a= (k*l)//nl
b= c*d
x= p//np

q=min(a,b,x)//n
print(q)
