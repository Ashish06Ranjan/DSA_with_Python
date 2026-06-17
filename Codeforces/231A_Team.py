"""
Problem : 231A. Team
Approach : First take the count = 0 and then we take the inputs and then we will apply condtition that if the result of adding those inputs is more than or equal to 2.
           Then we will increment the value of count to 1 else we will not increment anything .
           and then in the end we will print the value of count 

"""
n=int(input())

count=0
for _  in range(n):
    a,b,c=map(int,input().split())
    if a+b+c>=2:
        count+=1
    else:
        count+=0

print(count)
