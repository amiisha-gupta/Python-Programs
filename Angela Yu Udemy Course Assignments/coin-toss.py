import random

def coin_toss():
  flip_a_coin = int(input("\nDo you want to flip a coin?\n1.Yes\n2.No:\n"))
  if(flip_a_coin==1):
    print("\nYou flipped a coin. The result is:")
    result = random.randint(0,1)
    if(result): # ==1
      print("Heads")
    else:
      print("Tails")
    coin_toss()
  elif(flip_a_coin==2):
    print("Bye Bye!")
  else:
    print("invalid number.")
    coin_toss()
  
coin_toss()