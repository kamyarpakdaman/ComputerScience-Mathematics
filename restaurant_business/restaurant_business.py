# In this program, we define some classes for a chain restaurant
# to help structure the code and perform all business requirements.

# At first, we create our Menu class which includes different menus
# we can offer the customers, along with their names and availability time.

class Menu:

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        return '{name} menu is available from {start_time} to {end_time}'.format(name = self.name, start_time = self.start_time, end_time = self.end_time)
    
    # Calculating the price of the purchased items. Note that items is a 
    # dictionary including the names of menu items as keys and their prices
    # as values.
    def calculate_bill(self, purchased_items):
        self.total = 0
        for item in purchased_items:
            self.total += self.items[item]
        return (self.total)

# Here we create four menus.

# menu 1
brunch_dict = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu('brunch', brunch_dict, '11am', '4pm')

# menu 2
early_bird_dict = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
}
early_bird = Menu('early_bird', early_bird_dict, '3pm', '6pm')

# menu 3
dinner_dict = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
}
dinner = Menu('dinner', dinner_dict, '5pm', '11pm')

# menu 4
kids_dict = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu('kids', kids_dict, '11am', '9pm')

# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

# print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Then, we create the franchise class to better organize the data about our different
# franchise stores, each of which has an address and a set og menus.

class Franchise():

    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    def __repr__(self):
        return self.address
    
    # This function takes a time and lets customers know what menus are available
    # in a given franchise in a given time.
    def available_menus(self, time):
        self.available_menus_list = []
        if time in ['11am', '12am', '1pm', '2pm']:
            for item in self.menus:
                if item == brunch or item == kids:
                    if item not in self.available_menus_list:
                        self.available_menus_list.append(item.name)
                    else: continue
        elif time in ['5pm', '6pm']:
            for item in self.menus:
                if item == early_bird or item == dinner or item == kids:
                    if item not in self.available_menus_list:
                        self.available_menus_list.append(item.name)
                    else: continue
        elif time in ['7pm', '8pm', '9pm']:
            for item in self.menus:
                if item == dinner or item == kids:
                    if item not in self.available_menus_list:
                        self.available_menus_list.append(item.name)
                    else: continue
        elif time in ['10pm', '11pm']:
            for item in self.menus:
                if item == dinner:
                    if item not in self.available_menus_list:
                        self.available_menus_list.append(item.name)
                    else: continue
        return (self.available_menus_list)

# Here we create two franchises.

# franchise 1
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

# franchise 2
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

# print(flagship_store.available_menus('12am'))

# print(flagship_store.available_menus('5pm'))

# Finally, we're developing the business and we create a class named business
# to include the related franchises together in it.

class Business:

  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

# Creating a business for the chain restaurants.

Business_1 = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Eventualy, we will make a new business for making arepas.

# Creating a menu for arepas.

take_a_arepa_dict = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu('take a arepa', take_a_arepa_dict, '10am', '8pm')

# Creating a franchise for arepas.

arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

# Creating a business for arepas.
Business_2 = Business("Take a' Arepa", [arepas_place])

print('\nThanks for reviewing')

# Thanks for reviewing
