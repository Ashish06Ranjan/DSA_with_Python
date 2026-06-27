"""
Problem : 427A. Police Recruits
Approach :  Maintain a variable police to store the number of available police officers.
            Maintain another variable untreated to count crimes that cannot be handled.
            Traverse each event:
            If the event is positive, recruit that many officers (police += event).
            If the event is -1 (crime):
            If police > 0, assign one officer (police -= 1).
            Otherwise, increment untreated because no officer is available.
            After processing all events, print untreated.
            
"""
n = int(input())
events = list(map(int,input().split()))

police = 0 
untreated = 0 

for i in events :
  if i == -1 :
    if police > 0 :
      police -= 1
    else:
      untreated += 1
  else:
    police += i
print(untreated)
