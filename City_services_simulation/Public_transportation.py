class Bus:
  city_name = "Kansas City"
  base_fare = 1.5
  def __init__(self,route_number,passenger_capacity):
    self.route_number = route_number
    self.passenger_capacity = passenger_capacity
  
  def calculating_bus_fare(self, num_passengers):
    return self.base_fare * num_passengers