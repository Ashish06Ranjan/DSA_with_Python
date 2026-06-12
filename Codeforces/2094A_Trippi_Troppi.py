"""
Problem : 2094A Trippi Troppi

Approach : Taking the string input and printing the first letter by using the index 

"""

t=int(input())
 
for _ in range(t):
 
    x,y,z=input().split()
 
    print(x[0]+y[0]+z[0])
