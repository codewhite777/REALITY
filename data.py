calculation_to_units = 24
name_of_units = "hours"

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")
def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number ==0:
            print("you entered a 0,please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you ")
    except ValueError:
        print("your input is not a valid number, don't ruin my program")
        
user_input = ""
while user_input != "exit":
    user_input = input("hey user, enter a number of days and i will convert it to hours\n")
    print(type(set(user_input.split(", "))))
    # print(set(user_input.split(", ")))
    print(user_input.split(", "))
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()
        