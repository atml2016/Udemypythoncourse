print("Welcome to the roller coaster.")
height = int(input("Enter your height \n"))
bill = 0

if height>=120:
    print("You can ride the roller coaster")
    age = int(input("enter your age:\n"))
    if age<12:
        bill=5
        print("Child tickets are $5")
    elif 12<age<18:
        bill=10
        print("Youth tickets are $10")
    else:
        bill=20
        print("Adult tickets are $ 20")
    
    wants_photo = input("Do you want to have a photo take? type y for yes and n for no.").lower()

    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is {bill}")


else:
    print("Sorry you cant ride the coaster")