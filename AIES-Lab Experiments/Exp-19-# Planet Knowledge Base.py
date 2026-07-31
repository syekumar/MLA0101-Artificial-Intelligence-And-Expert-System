planet = {
    "Mercury": {
        "position": 1,
        "type": "Terrestrial",
        "moons": 0
    },
    "Earth": {
        "position": 3,
        "type": "Terrestrial",
        "moons": 1
    },
    "Mars": {
        "position": 4,
        "type": "Terrestrial",
        "moons": 2
    },
    "Jupiter": {
        "position": 5,
        "type": "Gas Giant",
        "moons": 95
    }
}

name = input("Enter planet name: ")

if name in planet:
    print("Planet:", name)
    print("Position from Sun:", planet[name]["position"])
    print("Type:", planet[name]["type"])
    print("Number of Moons:", planet[name]["moons"])
else:
    print("Planet not found in Knowledge Base")
