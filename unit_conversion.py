def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def inches_to_centimeters(inches):
    return inches * 2.54

def centimeters_to_inches(centimeters):
    return centimeters / 2.54

def main():
    while True:
        # Display operation options
        print("\nSelect conversion type:")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        print("3. Inches to Centimeters")
        print("4. Centimeters to Inches")
        print("5. Exit")

        # Get user's choice
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}° Fahrenheit is equal to {celsius:.2f}° Celsius")
        
        elif choice == '2':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}° Celsius is equal to {fahrenheit:.2f}° Fahrenheit")
        
        elif choice == '3':
            inches = float(input("Enter length in inches: "))
            centimeters = inches_to_centimeters(inches)
            print(f"{inches} inches is equal to {centimeters:.2f} centimeters")
        
        elif choice == '4':
            centimeters = float(input("Enter length in centimeters: "))
            inches = centimeters_to_inches(centimeters)
            print(f"{centimeters} centimeters is equal to {inches:.2f} inches")
        
        elif choice == '5':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
