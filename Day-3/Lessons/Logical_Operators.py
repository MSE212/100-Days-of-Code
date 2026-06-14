print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")

    age = int(input("What is your age? "))
    
    if age < 12:
        print("Please pay $5")
        bill = 5
    elif age <= 18:
        print("Please pay $7")
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
    else:
        print("Please pay $12")
        bill = 12

    photos = input("Do you want photos? Y/N\n")
    
    if photos == 'Y' and bill != 0:
        bill += 3
        print(f"The total bill is ${bill}")
    else:
        print(f"Your total bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")