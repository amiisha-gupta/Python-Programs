def Remaining_Weeks():

    age = int(input("\nEnter your age:\n"))
    
    total_weeks = 90*52
    weeks_lived = age*52
    weeks_left = total_weeks - weeks_lived
    
    print(f"You have {weeks_left} weeks left.")
    Remaining_Weeks()
    
Remaining_Weeks()