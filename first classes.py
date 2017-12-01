# first classes
class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print ("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

  def is_edible(self):
    if not self.poisonous:
      print ("Yep! I'm edible.")
    else:
      print ("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

# Animals


class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health="good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print( self.name )
    print(self.age)
          

    
    
hippo=Animal('Popi', 6)
sloth=Animal('suzi', 5)
ocelot=Animal('Kozer', 7)

print (hippo.health)
print (sloth.health)
print (ocelot.health)




