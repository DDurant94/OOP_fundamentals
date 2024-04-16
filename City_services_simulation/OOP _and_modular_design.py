'''
3. City Services Simulation: Python OOP and Modular Design
Objective:
This assignment aims to strengthen your skills in Python Object-Oriented Programming (OOP) and modular programming 
by building a simulation of city services. The focus will be on using class variables and organizing code into modules, 
simulating services like public transportation, park management, and city utilities.

Task 1: Public Transportation Module

Problem Statement: Develop a Bus class as part of a public transportation module. Use class variables to represent 
common attributes like city name and base fare. Implement instance variables for specific attributes like route number and passenger capacity.
Expected Outcome: A Bus class with both class and instance variables, and a transportation module to manage different bus routes. 
A test script should demonstrate creating bus instances and accessing both class and instance attributes.
'''

from Public_transportation import Bus
buses = ["001", "002", "003"]
routes = ["101","102","103"]
print("Bus availability: ")
for count,bus in enumerate(buses):
  print(f"{count+1}. Bus#{bus}")
user_input = input("Choose a bus [000]: ")
print("Bus Routes:")
for count, route in enumerate(routes):
  print(f"{count+1}. {route}")
user_input1 = input("Choose a route number [000]: ")
user_input2 = int(input("Enter passenger capacity: "))
user_input = Bus(user_input1,user_input2)
passenger_count = int(input("How many people are on the bus: "))
if passenger_count < user_input2:
  total_fare = user_input.calculating_bus_fare(passenger_count)
  print(f"The total fare is ${total_fare} in {user_input.city_name} on route #{user_input1}. With a passenger count of {passenger_count} people")
else:
  print("Can Not have more passengers than you can carry")
