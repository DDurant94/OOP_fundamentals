class Building:
  def __init__(self, name, floors):
    self.name = name
    self.floors = floors

  def export_file(self,file):
    try:
      with open(file, 'a') as file:
        print(file)
        file.write(f"{self.name},{self.floors}\n")
        print(f"File has been saved")
    except:
      pass
  def import_file(self,file):
    try:
      with open(file, "r") as file:
        buildings = []
        for line in file:
          name,floors = line.strip().split(',')
          buildings.append(line)
        return buildings
    except AttributeError:
      pass

  
