n1 = int(input())
n2 = int(input())
n3 = int(input())

m1 = 0
m2 = 0
m3 = 0
i = 0
if(n1>n2) and (n1 > n3):
  m1 = n1
  if(n2>n3):
    m2 = n2
    m3 = n3
  else:
    m2 = n3
    m3 = n2
    
elif(n2>n1) and (n2>n3):
  m2= n2
  if(n1>n3):
    m2 = n1
    m3 = n3
  else:
    m2 = n3
    m3 = n1

else:
  m1 = n3
  if(n1>n3):
    m2 = n1
    m3 = n3
  else:
    m2 = n2
    m3 = n1

#Testando
if(i == 1):
  print(m3, m2, m1)
elif(i == 2):
  print(m1, m2, m3)
else:
  print(m2, m1, m3)
      
      
 
