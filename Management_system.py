'''
1. City Infrastructure Management System
Objective:
The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build 
a simulated City Infrastructure Management System. This system will incorporate classes, objects, methods, 
and data structures to manage different aspects of a city, such as buildings, traffic, and events.

Task 1: Vehicle Registration System

Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.
Code Example: Provide a basic structure for the Vehicle class without methods.
```python
class Vehicle:
def init(self, reg_num, type, owner):
self.registration_number = reg_num
self.type = type
self.owner = owner
```
Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script 
showing the creation of Vehicle objects and updating their owners.

Task 2: Event Management System Enhancement

Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. 
Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
Code Example: Basic Event class without participant tracking.
```python
class Event:
def init(self, name, date):
self.name = name
self.date = date
```
'''

class Vehicle:
  def __init__(self, reg_num, type, owner):
    self.registration_number = reg_num
    self.type = type
    self.owner = owner

  def update_owner(self,new_owner):
    self.owner = new_owner

vehicle1 = Vehicle("JTC-112","Truck", "Jim")
vehicle2 = Vehicle("ATR-234","Car","Kristen")
vehicle3 = Vehicle("GFD-764","Motorcycle","David")

print(f"Vehicle1 (Type of vehicle: {vehicle1.type}) with a (Registration number {vehicle1.registration_number}): Owner is {vehicle1.owner}")
print(f"Vehicle2 (Type of vehicle: {vehicle2.type}) with a (Registration number {vehicle2.registration_number}): Owner is {vehicle2.owner}")
print(f"Vehicle3 (Type of vehicle: {vehicle3.type}) with a (Registration number {vehicle3.registration_number}): Owner is {vehicle3.owner}")

vehicle1.update_owner("Tom")
vehicle2.update_owner("Kathy")
vehicle3.update_owner("Tara")

print(f"The updated owner of vehicle1 is {vehicle1.owner} (Registration number {vehicle1.registration_number})")
print(f"The updated owner of vehicle2 is {vehicle2.owner} Registration number {vehicle2.registration_number})")
print(f"The updated owner of vehicle3 is {vehicle3.owner} (Registration number {vehicle3.registration_number})")


# Task Two

class Event:
  def __init__(self, name, date):
    self.name = name
    self.date = date
    self.participant_count = 0

  def add_participant(self,person):
    participants = []
    participants.append(person)
    self.participant_count += 1
    return participants

  def get_participant_count(self):
    return self.participant_count

event_name = input("Enter the event name: ").title()
event_date = input("Enter the date [YYYY-MM-DD]: ")
event = Event(event_name,event_date)
while True:
  user_choice = input("Do you want to enter in more people for this even: [Y/N] ").upper()
  if user_choice == "Y":
    participants = input("Enter participants name: ").title()
    people_attending = event.add_participant(participants)
    print(f"People Attending {event_name} on {event_date}:")
    for people in people_attending:
      print(f"{people}")
    print(f"{event.get_participant_count()}")
  else:
    break
