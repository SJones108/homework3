def calculate_square_footage(rooms):
    total_area = 0
    for room in rooms:
        room_width = float(input(f"What is the width of {room} (in feet)?: "))
        room_length = float(input(f"What is the length of {room} (in feet)?: "))
        room_area = room_width * room_length
        print(f"The area of {room} is {room_area} square feet.")
        total_area += room_area
    print(f"The total square footage of the house is {total_area} square feet.")

def calculate_circumference(radius):
    pi = 3.14159
    circumference = 2 * pi * radius
    return circumference
