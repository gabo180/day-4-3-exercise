# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
list_position = [int(a) for a in str(position)]
map[list_position[1] - 1] [list_position[0] - 1] = "X"

# Teacher solution:
# horizontal =  int(position[0])
# vertical = int(position[1])

#map[vertical - 1][horizontal - 1] = "X" ## Another solution

#selected_row = map[vertical - 1]
#selected_row[horzintal - 1] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")