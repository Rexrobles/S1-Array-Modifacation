# Write a python program that do the following:

# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array


# Note: 
# - The program has an array variable containing 10 random numbers
# - You may add other options and features
# - Your program should be uploaded to github before 1:30pm
# - Record a demo presenting your program
# - Send the demo directly to my messenger

# Example Output:

# Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
# Menu:
# 1 -> Add an element
# 2 -> Insert an element
# 3 -> Modify an element
# 4 -> Delete an element
# 5 -> Arrange in ascending order
# 6 -> Arrange in descending order
# What do you want to do? (1-6): 4
# Enter the index you want to delete: 3
# The element has been deleted
# This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]



print("""
  Menu:
  1 -> Add an element
  2 -> Insert an element
  3 -> Modify an element
  4 -> Delete an element
  5 -> Total sum of element
  6 -> define the largest element
  7 -> Arrange in ascending order
  8 -> Arrange in descending order
  9 -> count the times the element appears
""")

List_Value = [14, 3, 15, 27, 14, 10, 6, 24, 100, 5]

print(f"List: {List_Value}")

menuInput = int(input("What do you want to do? (1-9): "))
if menuInput not in range(1, 10):
        print("Invalid! Please enter 1 to 9 only.")

if menuInput == 1:
    numberAdd = int(input("Enter the number you want to add: "))
    List_Value.append(numberAdd)
    print("The element has been added.")
    print(f"This is the new array. Array = {List_Value}")
    
elif menuInput == 2:
    numberInsert = int(input("Enter the number you want to insert: "))
    indexInsert = int(input(f"Enter the index you want to insert {numberInsert}: "))
    List_Value.insert(indexInsert, numberInsert)
    print("The element has been inserted.")
    print(f"This is the new array. Array = {List_Value}")
    
elif menuInput == 3:
    indexModify = int(input("Enter the index you want to modify: "))
    numberModify = int(input(f"Enter the number you want to change in index {indexModify}: "))
    List_Value[indexModify] = numberModify
    print("The element has been modified.")
    print(f"This is the new array. Array = {List_Value}")
    
elif menuInput == 4:
    indexDelete = int(input("Enter the index you want to delete: "))
    List_Value.pop(indexDelete)
    print("The element has been deleted.")
    print(f"This is the new array. Array = {List_Value}")
    
elif menuInput == 5:
    Total = sum(List_Value)
    print("This is the total sum of all element")
    print(f"The total sum is = {Total}")
    
elif menuInput == 6:
    largest = max(List_Value)
    print("The list has Define the largest Number.")
    print(f"The Largest Number is = {largest}")
    
elif menuInput == 7:
    List_Value.sort()
    print("The list has been arranged in ascending order.")
    print(f"This is the new array. Array = {List_Value}")
    
elif menuInput == 8:
    List_Value.reverse()
    print("The list has been arranged in descending order.")
    print(f"This is the new array. Array = {List_Value}")
    
elif menuInput == 9:
    numberInputCount = int(input("Enter the number for which you want to know the occurrence in the list: "))
    numberCount = List_Value.count(numberInputCount)
    print(f"The number {numberInputCount} was shown {numberCount} times in the list.")
