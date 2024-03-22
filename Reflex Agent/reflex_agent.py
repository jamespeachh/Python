import random


class Environment(object):
    def __init__(self):
        self.dirtyRoom = {'A': '0', 'B': '0'}
        self.dirtyRoom['A'] = random.randint(0, 1)
        self.dirtyRoom['B'] = random.randint(0, 1)


class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        rooms_cleaned = 0
        vacuumLocation = random.randint(0, 1)
        if vacuumLocation == 0:
            self.room_check(Environment, rooms_cleaned, 'A', 'B')
        elif vacuumLocation == 1:
            self.room_check(Environment, rooms_cleaned, 'B', 'A')
    
    def room_check(self, Environment, rooms_cleaned, first_room, second_room):
        print(f"Vacuum randomly placed at Location {first_room}.")
        print(f"Location {first_room} is Dirty.") \
            if Environment.dirtyRoom[first_room] == 1 else print(f"Location {first_room} is Clean.")
        if Environment.dirtyRoom[first_room] == 1:
            Environment.dirtyRoom[first_room] = 0
            rooms_cleaned += 1
            print(f"Location {first_room} has been Cleaned.")
        print(f"Moving to Location {second_room}...")
        print(f"Location {second_room} is Dirty.") \
            if Environment.dirtyRoom[second_room] == 1 else print(f"Location {second_room} is Clean.")
        if Environment.dirtyRoom[second_room] == 1:
            Environment.dirtyRoom[second_room] = 0
            rooms_cleaned += 1
            print(f"Location {second_room} has been Cleaned.")
        print("Environment is Clean.")

        print(Environment.dirtyRoom)
        print("Performance Measurement: " + str(rooms_cleaned))


theEnvironment = Environment()
theVacuum = SimpleReflexVacuumAgent(theEnvironment)
