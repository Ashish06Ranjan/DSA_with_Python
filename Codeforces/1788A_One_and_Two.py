"""
Problem : 1788A. One and Two
Approach : Count the total number of 2s in the array.
            If the count of 2s is odd, it is impossible to split the product equally, so print -1.
            If there are no 2s, all elements are 1, so any split works. Print 1.
            Otherwise, find the position where half of the total 2s have been seen.
            That position gives the smallest valid k.
"""
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total_twos = a.count(2)

    if total_twos % 2 == 1:
        print(-1)
    elif total_twos == 0:
        print(1)
    else:
        need = total_twos // 2
        cnt = 0

        for i in range(n):
            if a[i] == 2:
                cnt += 1

            if cnt == need:
                print(i + 1)
                break
