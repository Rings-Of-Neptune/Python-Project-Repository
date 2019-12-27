class Menu():
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def __repr__(self):
    return "{} menu available from {}00 to {}00.".format(self.name, self.start_time, self.end_time)
  
  def calculate_bill(self, purchased_items):
    self.purchased_items = purchased_items
    billTotal = 0
    for i in purchased_items:
      billTotal += self.items[i]
    return billTotal
  
class Franchise():
  def __init__(self, address, menu):
    self.address = address
    self.menu = menu
    
  def __repr__(self):
    return "Located at {}.".format(self.address)
  
  def available_menus(self, time):
    available_results = []
    for i in self.menu:
      if time < i.end_time and time > i.start_time:
        available_results.append(i)
    return available_results
  
class Business():
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

brunch = Menu('brunch', {'pancakes':7.50, 'waffles':9.00, 'burger':11.00, 'home fries':4.50, 'coffee':1.50, 'espresso':3.00, 'tea':1.00, 'mimosa':10.50, 'orange juice':3.50}, 11, 16)

early_bird = Menu('early_bird', {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 15, 18)

dinner = Menu('dinner', {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 5, 23)

kids = Menu('kids', {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

arepas_menu = Menu('arepas_menu', {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 10, 20)

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

Basta = Business("Basta Fazoolin with my Heart", [flagship_store, new_installment])
