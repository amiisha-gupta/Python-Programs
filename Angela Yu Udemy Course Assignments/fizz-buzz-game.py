def FizzBuzzGame():

  num = 1
  num2 = 100 #Default value
  
  num2 = int(input("\nEnter a number:\n"))

  while(num<=num2):
    if num%3==0 and num%5==0:
      print("FizzBuzz")
    elif num%5==0:
      print("Buzz")
    elif num%3==0:
      print("Fizz")
    else:
      print(num)
    num+=1
    
  FizzBuzzGame()
  
FizzBuzzGame()