def area_of_circle(radius):
    pi= 3.14
    """Calculates the area of a circle.

  Args:
    radius: The radius of the circle.

  Returns:
    The area of the circle.
  """

    circumference = 2 * pi * radius
    area = circumference * radius / 2
    return area


# Example usage:

radius = 5
area = area_of_circle(radius)

print("The area of the circle is:", area)
