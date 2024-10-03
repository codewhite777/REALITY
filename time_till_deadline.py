import datetime

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")
goal =input_list[0]
deadline = input_list[1]
# try:
# except ValueError():
# lookup the documentation of the module
deadline_date =datetime.datetime.strptime(deadline, "%d.%m.%Y")
# print(type(datetime.datetime.strptime(deadline, "%d.%m.%Y")))
# print(input_list)
today_date = datetime.datetime.now()
# calculate how many days from now to deadline
time_till =deadline_date-today_date
# hours_till = {int(time_till.total_seconds()/60/60)}
print(f"Dear user! Time remaining for your:{goal} is {time_till.days} days")
print(f"Dear user! Time remaining for your:{goal} is {int(time_till.total_seconds()/60/60)} hours")

# built in vs third party packages
# web application=django
# note you can find this packages or modules from pypi.org
# difference between module and packages
# module is basically python files we create by ourself 
# package is a collection of python modules and it contains multiple python file and we can use it anytime{note package is more structured }
# pypi(the python package index) is a repository(storage) for third party python packages and people can publish their packages to this repository
# so that it become available for other programmers to use
# a large community means many people are creating useful modules and make them available for others
# note we use pip to instal package in python e.g {pip install django}
# pip is a package manager for python
# for javascript is npm 
# for java is 

 