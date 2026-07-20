# Birds Fly Knowledge Base

# Birds
birds = {"sparrow", "parrot", "penguin", "ostrich"}

# Birds that cannot fly
cannot_fly = {"penguin", "ostrich"}

# Function to check flying ability
def can_fly(animal):
    if animal in birds:
        if animal in cannot_fly:
            return False
        return True
    return None

# Test cases
animals = ["sparrow", "parrot", "penguin", "ostrich"]

for a in animals:
    if can_fly(a):
        print(a, "can fly")
    else:
        print(a, "cannot fly")
