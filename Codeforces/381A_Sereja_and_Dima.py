"""
Problem : 381A. Sereja and Dima
Approach :  Use two pointers:
            l = 0 (left end)   r = n-1 (right end)
            Sereja and Dima play alternately.
            On each turn, compare a[l] and a[r].
            Take the larger card.
            Move the corresponding pointer.
            Add the chosen card to the current player's score.
            Continue until all cards are taken.
            Print Sereja's score and Dima's score.

"""

n = int(input())
a = list(map(int,input().split()))

l = 0
r = n-1

sereja = 0 
dima = 0 
turn = 0

while l<=r:
  if a[l] > a[r]:
        card = a[l]
        l += 1
    else:
        card = a[r]
        r -= 1

    if turn % 2 == 0:
        sereja += card
    else:
        dima += card

    turn += 1

print(sereja, dima)
