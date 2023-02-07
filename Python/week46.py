"""
Coordinates start at 0,0. The first movement is on the Y-axis,
for each movement, it rotates 90º counterclockwise.
"""

x, y = (0, 0)

user_moves = [0, ]
print("Insert a number, otherwise it'll finish.")
while True:
    try:
        new = int(input("Insert a number: "))
    except ValueError:
        break
    else:
        user_moves.append(new)

for pos, move in enumerate(user_moves):
    print(pos, move)
    if pos % 4 == 1:
        y += move
    elif pos % 4 == 2:
        x -= move
    elif pos % 4 == 3:
        y -= move
    elif pos % 4 == 0:
        x += move

robot_coordinates = (x, y)
print(f"Your robot is at the position {robot_coordinates}")
