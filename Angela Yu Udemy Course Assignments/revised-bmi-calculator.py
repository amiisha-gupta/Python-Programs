def BMI_Calculator():
  height = float(input("\nEnter your height in metres: (e.g:1.65)\n"))
  weight = int(input("\nEnter your weight in kilograms: (e.g:72)\n"))
  bmi = weight/(height*height)# Alternately, height**2 can be written
  bmi = int(bmi) # converting to an integer
  
  if(bmi<18.5):
    print(f"Your BMI is {bmi}, you are underweight.")
  if(bmi>=18.5 and bmi<25):
    print(f"Your BMI is {bmi}, you have a normal weight.")
  if(bmi>=25 and bmi<30):
    print(f"Your BMI is {bmi}, you are slightly overweight.")
  if(bmi>=30 and bmi<35):
    print(f"Your BMI is {bmi}, you are obese.")
  if(bmi>=35):
    print(f"Your BMI is {bmi}, you are clinically obese.")

  BMI_Calculator()
  
BMI_Calculator()