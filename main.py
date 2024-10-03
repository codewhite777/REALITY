# import sys
# sys.exit() 
# calculations_to_seconds = 23 * 50
# name_of_units = "minutes"

# def days_to_units(num_of_days):
#     if num_of_days < 0:
#        print(f"{num_of_days}  days are {50 * calculations_to_seconds} {name_of_units}")
#        # print(f"{num_of_days} 20 days are {50 * calculations_to_seconds} {name_of_units}")/
# #        # print(f"20 days are {50 * calculations_to_seconds} {name_of_units}")
# #        return ("all good")
# # days_to_units(50)  
# # days_to_units(21)  
# # days_to_units(30)  
# # days_to_units(40)  
# # days_to_units(60)  
# # # 2 WAYS TO INPUT 
# # user_input = input("who is your love?")
# # print(user_input)
# # print(input("what is your name? "))

# # input(" HEY! whats your name? ")
# # if input == " nwankwo ":
# #    print(input)

# print(type(10))
  
#   nested if...else statement 
# try/except statement is also called try/catch in other programming languages it catches error

from numpy import append


try:
    user = (input("enter username: "))
    # while user != "exit":
    if user=="ifeanyi":
        print("welcome")

    elif user !="ifeanyi": 
        print("incorrect") 
          
except ValueError:
    pass
# list
try:
  list_of_integers =[10,12,12 ]
  list_of_integers.remove(12)
  print(list_of_integers)
  list_of_integers.append(4)
  print(list_of_integers)
  my_list =["january","february","march"]
  print(my_list[2])
except IndexError: 
  print(my_list[5])
  print(my_list)
  #thanks jetbrains and space
# study build in function