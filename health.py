#health potion example
import random
health = 50
difficulty = 3
potion_health = int (random.randint(25,50)/difficulty) #Casting to INT #Division always gives float

print (potion_health)
health = (health + potion_health)
print ("Health is " , health, " points")
message = ' I am here doing "python programming" '
print (message)
