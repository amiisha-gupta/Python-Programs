def Treasure_Game():
    
    print("\nWelcome to treasure island.\nChoose your own adventure!\nYou came across an abandoned mansion.\n")
    choice1 = int(input("There are two doors labeled '1' and '2'.\nMake your choice:\n"))
    choice2 = choice3 = choice4 = 1
    coins = 0
    play_again = 0
    if(choice1==1):
        choice2 = int(input("The room was empty.\n\nThere are two doors labeled '1' and '2'.\nMake your choice:\n"))
        if(choice2==1):
            choice3 = int(input("You found 15 coins.\n\nThere are two doors labeled '1' and '2'.\nMake your choice:\n"))
            coins+=15
            if(choice3==1):
                print(f"You came across a Dead End.\n\nTotal coins: {coins}")
            if(choice3==2):
                choice4 = int(input("You found 50 coins.\n\nThere are two doors labeled '1' and '2'.\nMake your choice:\n"))
                coins+=50
                if(choice4==1):
                    coins+=50000000
                    print(f"You found 50000000 coins. Total coins: {coins}")
                if(choice4==2):
                    print(f"You came across a Dead End.\n\nTotal coins: {coins}")       
        if(choice2==2):
            print(f"You came across a Dead End.\n\nTotal coins: {coins}")
    if(choice1==2):
        choice2 = int(input("You found 100 coins.\n\nThere are two doors labeled '1' and '2'.\nMake your choice:\n"))
        coins+=100
        if(choice2==1):
            choice3 = int(input("You found 5 coins.\n\nThere are two doors labeled '1' and '2'.\nMake your choice:\n"))
            coins+=5
            if(choice3==1):
                print(f"You came across a Dead End.\n\nTotal coins: {coins}")
            if(choice3==2):
                choice4 = int(input("You found 50 coins.\n\nThere are two doors labeled '1' and '2'.\nMake your choice:\n"))
                coins+=50
                if(choice4==1):
                    coins+=100000
                    print(f"You found 100000 coins. Total coins: {coins}")
                if(choice4==2):
                    print(f"You came across a Dead End.\n\nTotal coins: {coins}")      
        if(choice2==2):
            print(f"You came across a Dead End.\n\nTotal coins: {coins}")
            
    if(choice1<1 or choice1>2 or choice2<1 or choice2>2 or choice3<1 or choice3>2 or choice4<1 or choice4>2):
        print(f"There were only two doors. You bumped into a wall trying to look for more doors. Total coins: {coins}")
    
    play_again = input("\nWould you like to play the game again?\nEnter 1 to play the game again.\n")
    if(play_again=='1'):
        Treasure_Game()
    else:
        print("Bye Bye!")
    
Treasure_Game()