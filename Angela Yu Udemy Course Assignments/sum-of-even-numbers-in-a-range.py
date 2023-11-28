def Sum_of_Even_Numbers():

  target = int(input("\nEnter a number between 0 to 1000:\n"))

  sum = 0
  next = 2

  if target<=1000:
    while next<=target:
      sum+=next
      next+=2
    print(f"The sum of all even numbers between 0 and {target} is: {sum}")
  else:
    print("Number too large.")

  Sum_of_Even_Numbers()

Sum_of_Even_Numbers()