# Let's define the class Bike
class Bike:
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material

    def brake(self):
        print("Braking!!")
    
    def describe(self):
        print(self.colour)
        print(self.frame_material)

# let's create a couple of instances
red_bike = Bike('Red', 'carbon fiber')
blue_bike = Bike('Blue', 'Steel')

# let's inspect the objects we have, instances of the bike class
red_bike.describe()
blue_bike.describe()

# let's brake
red_bike.brake()