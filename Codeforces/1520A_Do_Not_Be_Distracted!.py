"""
Problem : 1520A. Do Not Be Distracted!
Approach : We need to make sure that each task appears in only one continuous block.
          Traverse the string:
          Whenever the current character is different from the previous one, it means we are starting a new task block.
          If that task was already seen before, it means Polycarp returned to a previous task → print "NO".
          Otherwise, mark it as seen.
          If we finish the string without any repetition of a finished task → print "YES".

"""

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    seen = []
    possible = True

    for i in range(n):
        if i == 0 or s[i] != s[i-1]:
            if s[i] in seen:
                possible = False
                break
            seen.append(s[i])

    if possible:
        print("YES")
    else:
        print("NO")
