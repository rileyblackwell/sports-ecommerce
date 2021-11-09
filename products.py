class Product(object):
    def __init__(self, name):
        self.price = None
        self.color = None
        self.size = None
        self.name = name
    
    def set_price(self, price):
        self.price = price
    
    def set_color(self, color):
        self.color = color
    
    def set_size(self, size):
        self.size = size 

    def get_price(self):
        return self.price
    
    def get_color(self):
        return self.color 
    
    def get_size(self):
        return self.size  

    def get_name(self) :
        return self.name     


class Sport(object):
    def __init__(self):
        self.helmet = Product('helmet')
        self.gloves = Product('gloves')
        self.elbow_pads = Product('elbow_pads')
        self.knee_pads = Product('knee_pads')
        self.mouth_guard = Product('mouth_guard')
        self.items = {}
        self.items[self.helmet.get_name()] = self.helmet
        self.items[self.gloves.get_name()] = self.gloves
        self.items[self.elbow_pads.get_name()] = self.elbow_pads
        self.items[self.knee_pads.get_name()] = self.knee_pads
        self.items[self.mouth_guard.get_name()] = self.mouth_guard
    
    def set_item_price(self, item, price):
        try: 
            item_object = self.items[item] 
            item_object.set_price(price)
        except KeyError:
            print('Key not in dictionary!')
             
    def get_item_price(self, item):
        try: 
            item_object = self.items[item] 
            return item_object.get_price()
        except KeyError:
            print('Key not in dictionary!')

    def set_item_color(self, item, color):
        try: 
            item_object = self.items[item] 
            item_object.set_color(color)
        except KeyError:
            print('Key not in dictionary!')
             
    def get_item_color(self, item):
        try: 
            item_object = self.items[item] 
            return item_object.get_color()
        except KeyError:
            print('Key not in dictionary!')
    
    def set_item_size(self, item, size):
        try: 
            item_object = self.items[item] 
            item_object.set_price(size)
        except KeyError:
            print('Key not in dictionary!')
             
    def get_item_size(self, item):
        try: 
            item_object = self.items[item] 
            return item_object.get_size()
        except KeyError:
            print('Key not in dictionary!')                   


class Hockey(Sport):
    def __init__(self):
        Sport.__init__(self)
        self.skates = Product('skates')
        self.items[self.skates.get_name()] = self.skates 
  
    
    
rebook = Hockey()

rebook.set_item_price('skates', 750)

print(rebook.get_item_price('skates'))
 
 

 
