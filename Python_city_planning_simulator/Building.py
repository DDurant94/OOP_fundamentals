class Building:
  def __init__(self, name, floors):
    self.name = name
    self.floors = floors
    self.building_info = {}

  def export_file(self,file):
    try:
      with open(file, 'a') as file:
        file.write(f"{self.name},{self.floors}\n")
        print(f"file has been saved")
    except FileNotFoundError:
      pass

  def import_file(self,file):
    try:
      with open(file, "r") as file:
        for line in file:
          name,floors = line.strip().split(',')
          self.building_info[name] = floors
        print(f"file has been loaded") 
        return self.building_info
    except AttributeError:
      pass

  
