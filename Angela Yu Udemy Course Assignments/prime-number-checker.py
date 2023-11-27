def prime_checker():
  number = int(input("Enter a number: "))
  i=2
  prime_num=True
  while(i!=number and prime_num==True):
    if number%i==0:
      print("It's not a prime number.")
      prime_num=False
    i+=1    
  if i==number:
    print("It's a prime number.")
    
  prime_checker()
    
prime_checker()