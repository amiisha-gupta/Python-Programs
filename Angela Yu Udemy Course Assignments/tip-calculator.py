def Tip_Calculator():
    print("\nWelcome to the tip calculator.")
    bill = float(input("What was the total bill? $"))
    tip_per = float(input("What percentage tip would you like to give?\n"))
    people = int(input("How many people to split the bill?\n"))
    tip = bill * tip_per/100
    bill_split = round((bill+tip)/people,2)
    bill_split = "{:.2f}".format(bill_split)
    print(f"Each person should pay ${bill_split}")
    Tip_Calculator()
    
Tip_Calculator()