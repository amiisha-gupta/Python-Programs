# code to add the digits of a two digit number, e.g. if the input is 93, output would 12.
def Add_Digits():
    two_digit_number = input("Enter a two-digit number: ")

    two_digit_number = int(two_digit_number)
    digit1 = int(two_digit_number/10)
    digit2 = two_digit_number%10
    print(digit1 + digit2)
    Add_Digits()

Add_Digits()
