# Programming Project 1
# Chase Forrest

while True:
    print("Choose conversion type:")
    print("1 Fahrenheit to Celsius")
    print("2 Celsius to Fahrenheit")
    print("3 Pounds to kilograms")
    print("4 Kilograms to pounds")
    print("5 Feet to meters")
    print("0 Goodbye!")

    user_choice = int(input("Enter user_choice: "))

    if user_choice == 0:
        print("Goodbye!")
        break
    elif user_choice == 1:
        Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        Celsius = (Fahrenheit - 32) * 5/9
        print(f"{Fahrenheit} Fahrenheit is equal to {Celsius} Celsius")
    elif user_choice == 2:
        Celsius = float(input("Enter temperature in Celsius: "))
        Fahrenheit = (Celsius * 9/5) + 32
        print(f"{Celsius} Celsius is equal to {Fahrenheit} Fahrenheit")
    elif user_choice == 3:
        Pounds = float(input("Enter number of pounds: "))
        Kilograms = (Pounds * 0.453592)
        print(f"{Pounds} pounds is equal to {Kilograms} kilograms")
    elif user_choice == 4:
        Kilograms = float(input("Enter number of kilograms: "))
        Pounds = (Kilograms * 2.2046)
        print(f"{Kilograms} kilograms is equal to {Pounds} pounds")
    elif user_choice == 5:
        Feet = float(input("Enter distance in feet: "))
        Meters = (Feet * 0.3048)
        print(f"{Feet} feet is equal to {Meters} meters")
    else: 
        print("Invalid input")