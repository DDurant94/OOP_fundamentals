'''
2. Python City Planning Simulator
Objective:
The aim of this assignment is to solidify understanding of Python's Object-Oriented Programming concepts through the 
development of a simulated city planning system. This system will integrate the use of classes, objects, inheritance, 
and file handling to manage various city elements like buildings, traffic systems, and public events.

Task 1: File Handling for Building Records

Problem Statement: Implement a system to handle building records using file operations. Create a Building class and 
write a script to save and load building details to and from a file.
Code Example: Skeleton of the Building class.
```python
class Building:
def init(self, name, floors):
self.name = name
self.floors = floors
# Methods to save to file and load from file
```
Expected Outcome: A complete Building class with methods for saving to and loading details from a file. 
A script demonstrating saving multiple buildings to a file and then reading them back into the program.

'''
from Building import Building


def main():
  print("Welcome to the Building Record Keeping Program")
  building_name = input("Enter the name of the building: ").title()
  number_floors = input("Enter the number of floors: ")
  building = Building(building_name,number_floors)
  while True:
    try:
      print("Main Menu:\n1. View Building\n2. Save File\n3. Import File\n4. Exit")
      menu_choice = input("Choose one of our menu options: ")
      if menu_choice == "1":
        city = building.import_file("Python_city_planning_simulator\\building_records.txt")
        for count, (name,floors) in enumerate(city.items()):
          print(f"Building Number {count+1}.\nBuilding name: {name}\nNumber of floors: {floors}\n")
      elif menu_choice == "2":
        building.export_file("Python_city_planning_simulator\\building_records.txt")
      elif menu_choice == "3":
        city = building.import_file("Python_city_planning_simulator\\building_records.txt")
      elif menu_choice == "4":
        print("Thank you for using Building Record Keeping Program")
        break
      else:
        print("Invalid input")
    except UnboundLocalError:
      print("Error: Load a file before viewing or saving")

main()