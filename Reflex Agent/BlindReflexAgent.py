import random


class Environment(object):
    def __init__(self):
        self.room_index = {'Left': '0', 'Right': '0'}
        self.room_index['Left'] = random.randint(0, 1)
        self.room_index['Right'] = random.randint(0, 1)


class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        rooms_cleaned = 0
        vacuum_location = random.randint(0, 1)
        if vacuum_location > 0:
            vacuum_location -= 1
        self.room_check(Environment, rooms_cleaned, 'Left', 'Right')
        vacuum_location += 1
        self.room_check(Environment, rooms_cleaned, 'Right', 'Left')

    def room_check(self, Environment, rooms_cleaned, first_room, second_room):
        print(f"Vacuum randomly placed at Location {first_room}.")
        print(f"Location {first_room} is Dirty.") \
            if Environment.room_index[first_room] == 1 else print(f"Location {first_room} is Clean.")
        if Environment.room_index[first_room] == 1:
            Environment.room_index[first_room] = 0
            rooms_cleaned += 1
            print(f"Location {first_room} has been Cleaned.")
        print(f"Moving to Location {second_room}...")
        print(f"Location {second_room} is Dirty.") \
            if Environment.room_index[second_room] == 1 else print(f"Location {second_room} is Clean.")
        if Environment.room_index[second_room] == 1:
            Environment.room_index[second_room] = 0
            rooms_cleaned += 1
            print(f"Location {second_room} has been Cleaned.")
        print("Environment is Clean.")

        print(Environment.room_index)
        print("Performance Measurement: " + str(rooms_cleaned))


environment_init = Environment()
vacuum_init = SimpleReflexVacuumAgent(environment_init)
