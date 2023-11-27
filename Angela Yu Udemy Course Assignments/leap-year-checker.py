def Leap_Year():
  year = int(input("Enter the year: "))
  if(year%4==0 and year%400==0):
    print("Leap year")
  elif(year%4==0 and year%100==0):
    print("Not leap year")
  elif(year%4==0):
    print("Leap year")
  else:
    print("Not leap year")
  
  Leap_Year()
    
Leap_Year()