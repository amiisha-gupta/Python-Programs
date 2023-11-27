def Odd_Even_Number_Checker():
  number = int(input("Enter a number:\n"))
  remainder = number%2
  if(remainder!=0):
    print("This is an odd number.")
  if(remainder==0):
    print("This is an even number.")
  Odd_Even_Number_Checker()
  
Odd_Even_Number_Checker()