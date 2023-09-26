# Calculate the area of a triangle, rectangle, or circle

# Get the shape type from the user
shape = input("Enter the shape type (triangle, rectangle, or circle): ")

# Calculate the area based on the shape type
if shape == "triangle":

    # Get the base and height of the triangle from the user
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    # Calculate the area of the triangle
    area = 0.5 * base * height

elif shape == "rectangle":

    # Get the length and width of the rectangle from the user
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate the area of the rectangle
    area = length * width

elif shape == "circle":

    # Get the radius of the circle from the user
    radius = float(input("Enter the radius of the circle: "))

    # Calculate the area of the circle
    area = 3.14 * radius ** 2

else:

    print("Invalid shape type")

# Print the area to the console
print("The area of the shape is", area)



