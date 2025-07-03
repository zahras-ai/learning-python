# Get input from the user
user_input_string = input(
    "Enter numbers separated by spaces (e.g., 10 25 5): ")

# Split the string into a list of string elements
string_list = user_input_string.split()

# Convert each string element to an integer
try:
    numbers_list = list(map(int, string_list))
    sum = 0
    for number in numbers_list:
        sum += number
    average = sum/len(numbers_list)
    print("average is: ", average)
except ValueError:
    print("Invalid input. Please enter only numbers separated by spaces.")
