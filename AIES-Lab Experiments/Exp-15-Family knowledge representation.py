# Family Knowledge Representation

# Gender
male = {"John", "Mike", "Tom"}
female = {"Mary", "Anna", "Lisa"}

# Parent relationships
parent = {
    ("John", "Mike"),
    ("Mary", "Mike"),
    ("John", "Anna"),
    ("Mary", "Anna"),
    ("Mike", "Tom"),
    ("Lisa", "Tom")
}

# Functions
def father(x, y):
    return x in male and (x, y) in parent

def mother(x, y):
    return x in female and (x, y) in parent

def siblings(x, y):
    if x == y:
        return False
    px = {p for p, c in parent if c == x}
    py = {p for p, c in parent if c == y}
    return len(px & py) > 0

def grandfather(x, y):
    if x not in male:
        return False
    for p, c in parent:
        if c == y and (x, p) in parent:
            return True
    return False

# Test
print("Father(John, Mike):", father("John", "Mike"))
print("Mother(Mary, Anna):", mother("Mary", "Anna"))
print("Siblings(Mike, Anna):", siblings("Mike", "Anna"))
print("Grandfather(John, Tom):", grandfather("John", "Tom"))
