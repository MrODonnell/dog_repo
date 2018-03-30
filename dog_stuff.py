class Dog:
    """This is the beginning of a class for the best good boy ever, a doug
            Attributes:
            name
            weight
            food dish level

    """

    foodDishLevel = 100

    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

    def eat(self):
        self.foodDishLevel -= 10

    def compare(self, compare):
        self.compare = compare

    #add new def here for returning a value
    def cool(self):
        return 1


#this is the set of info for Mick
d = Dog('Mick')

d.add_weight(10)

c = ("Smart", "Awesome", "Strong", "Fast", "Likes to play")


#this is the set of info for woof
x = Dog('Woof')

x.add_weight(12)

y = ("Dumb", "Not cool", "Weak", "Slow", "Lazy")



print(d.name + " weighs: " + str(d.weight) + " pounds")
print(x.name + " weighs: " + str(x.weight) + " pounds")
print(" ")

x.eat()

print(d.name + " has " + str(d.foodDishLevel) + "% of their food left")
print(x.name + " has " + str(x.foodDishLevel) + "% of their food left")
print(" ")

print("Mick is: ")
for i in c:
    print(i)
print(" ")

print("Woof is: ")
for a in y:
    print(a)
print(" ")

d.compare = d.weight
x.compare = x.weight

if d.compare <= x.compare:
    return True

if d.compare >= x.compare:
    return False
