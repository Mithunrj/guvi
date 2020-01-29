source = int(input("enter the value of source:"))
destination = int(input("enter the value of destination:"))
i = 1
km = destination - source
print ("the total km travelled",km)
while (i>0):

  d = input("select the type of car :")
  if (d == 'mini'):
    total = km * 10
    print (total)
  elif (d == 'micro'):
    total = km * 25
      
    print (total)
  elif (d == 'prime'):
    total = km * 40 
      
    print (total)
  else:
      
    print ("select a valid car") 
    exit
  while (i>0):
      e = input("do you want to continue:")
      if (e == 'yes'):
        if (d == 'mini'):
          total = km * 10
          print (total)
        elif (d == 'micro'):
          total = km * 25
        
          print (total)
        elif (d == 'prime'):
          total = km * 40 
        
          print (total)
        else:
        
          print ("select a valid car") 
      else:
        i=i-1
        print("exit")     