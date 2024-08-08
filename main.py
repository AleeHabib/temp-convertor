def celsius_fahrenheit() -> None:

    try:
        temp = float(input("Enter temperature in Celsius: "))
    except ValueError:
        print("Enter a valid temperature!")

    temp_fah = (temp) * (9 / 5) + 32

    print(f"\nOriginal Temperature: {temp}°C")
    print(f"Converted Temperature: {temp_fah:.2f}°F")

    menu_option = input("\nEnter 'M' to go back: ")
    if menu_option.lower() == "m":
        temp_convertor()


def fahrenheit_celsius() -> None:

    try:
        temp = float(input("Enter temperature in Fahrenheit: "))
    except ValueError:
        print("Enter a valid temperature!")
    temp_celsius = (temp - 32) * (5 / 9)

    print(f"\nOriginal Temperature: {temp}°F")
    print(f"Converted Temperature: {temp_celsius:.2f}°C")

    menu_option = input("\nEnter 'M' to go back: ")
    if menu_option.lower() == "m":
        temp_convertor()


def celsius_kelvin() -> None:

    try:
        temp = float(input("Enter temperature in Celsius: "))
    except ValueError:
        print("Enter a valid temperature!")
    temp_kelvin = temp + 273.15

    print(f"\nOriginal Temperature: {temp}°C")
    print(f"Converted Temperature: {temp_kelvin:.2f}K")

    menu_option = input("\nEnter 'M' to go back: ")
    if menu_option.lower() == "m":
        temp_convertor()


def kelvin_celsius() -> None:

    try:
        temp = float(input("Enter temperature in Kelvin: "))
    except ValueError:
        print("Enter a valid temperature!")
    temp_celsius = temp - 273.15

    print(f"\nOriginal Temperature: {temp}K")
    print(f"Converted Temperature: {temp_celsius:.2f}°C")

    menu_option = input("\nEnter 'M' to go back: ")
    if menu_option.lower() == "m":
        temp_convertor()


def fahrenheit_kelvin() -> None:

    try:
        temp = float(input("Enter temperature in Fahrenheit: "))
    except ValueError:
        print("Enter a valid temperature!")

    temp_kelvin = (temp - 32) * (5 / 9) + 273.15

    print(f"\nOriginal Temperature: {temp}°F")
    print(f"Converted Temperature: {temp_kelvin:.2f}K")

    menu_option = input("\nEnter 'M' to go back: ")
    if menu_option.lower() == "m":
        temp_convertor()


def kelvin_fahrenheit() -> None:

    try:
        temp = float(input("Enter temperature in Kelvin: "))
    except ValueError:
        print("Enter a valid temperature!")
    temp_fahrenheit = (temp - 273.15) * (9 / 5) + 32

    print(f"\nOriginal Temperature: {temp}K")
    print(f"Converted Temperature: {temp_fahrenheit:.2f}°F")

    menu_option = input("\nEnter 'M' to go back: ")
    if menu_option.lower() == "m":
        temp_convertor()


def temp_convertor() -> None:

    print("\n------ CONVERSIONS ------")
    print("\n1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")
    print("3. Celsius -> Kelvin")
    print("4. Kelvin -> Celsius")
    print("5. Fahrenheit -> Kelvin")
    print("6. Kelvin -> Fahrenheit")
    print(" ")
    print("-------------------------")

    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            break
        except ValueError:
            print("Choice must be a valid integer, try again.")

    if choice == 1:
        celsius_fahrenheit()
    elif choice == 2:
        fahrenheit_celsius()
    elif choice == 3:
        celsius_kelvin()
    elif choice == 4:
        kelvin_celsius()
    elif choice == 5:
        fahrenheit_kelvin()
    elif choice == 6:
        kelvin_celsius()
    else:
        print("Enter a valid option")


if __name__ == "__main__":
    temp_convertor()
