'''When modeling something from the real world in code, you may find that 
you’re adding more and more detail to a class. You’ll find that you have a 
growing list of attributes and methods and that your files are becoming 
lengthy. In these situations, you might recognize that part of one class can 
be written as a separate class. You can break your large class into smaller 
classes that work together; this approach is called composition.
For example, if we continue adding detail to the ElectricCar class, we 
might notice that we’re adding many attributes and methods specific to 
the car’s battery. When we see this happening, we can stop and move those 
attributes and methods to a separate class called Battery. Then we can use a 
Battery instance as an attribute in the ElectricCar class
'''
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()