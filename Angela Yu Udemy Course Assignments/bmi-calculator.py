def BMI_Calculator():
    height = float(input("\nEnter your height in metres: (e.g:1.65)\n"))
    weight = int(input("\nEnter your weight in kilograms: (e.g:72)\n"))
    bmi = weight/(height*height)# Alternately, height**2 can be written
    bmi = int(bmi) # converting to an integer
    print(f"Your BMI is: {bmi}")
    BMI_Calculator()
    
BMI_Calculator()