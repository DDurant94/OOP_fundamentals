class Building:
  def __init__(self, name, floors):
    self.name = name
    self.floors = floors

  def export_file(self,file):
    try:
      with open(file, 'a') as file:
        file.write(f"{self.name},{self.floors}\n")
        print(f"file has been saved")
    except:
      pass

def import_file(file):
    try:
      with open(file, "r") as file:
        buildings = {}
        for line in file:
          name,floors = line.strip().split(',')
          buildings[name] = floors
        print(f"file has been loaded") 
        return buildings
    except AttributeError:
      pass

  
