try:
    MPH = float(input("Enter the wind speed in miles per hour: ")) 
except ValueError:
    print("Invalid input. Please enter a numeric value for the wind speed.")

MPH = float(input("Enter the wind speed in miles per hour: "))
if MPH > 157:
    print("Category 5 Hurricane")
elif MPH > 130:
    print("Category 4 Hurricane")
elif MPH > 111:
    print("Category 3 Hurricane")
elif MPH > 96:
    print("Category 2 Hurricane")
elif MPH > 74:
    print("Category 1 Hurricane")
else:
    print("Tropical storm")

