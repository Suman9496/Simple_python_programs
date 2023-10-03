# Get the conversion type from the user
conversion_type = input("Enter the conversion type (FtoC or CtoF): ")

# Get the temperature from the user
temperature = float(input("Enter the temperature: "))

# Convert the temperature based on the conversion type
if conversion_type == "FtoC":
  celsius = (5 / 9) * (temperature - 32)
  print("The temperature in Celsius is", celsius)
elif conversion_type == "CtoF":
  fahrenheit = (9 / 5) * temperature + 32
  print("The temperature in Fahrenheit is", fahrenheit)
else:
  print("Invalid conversion type")

