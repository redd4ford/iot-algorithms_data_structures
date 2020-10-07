class Helicopter:
    def __init__(self, name='no', max_passengers=0, max_speed=0):
        self.name = name
        self.max_passengers = max_passengers
        self.max_speed = max_speed

    def __str__(self):
        return 'Helicopter(name=' + self.name +\
               ', max_passengers=' + str(self.max_passengers) +\
               ', max_speed=' + str(self.max_speed) + ')'
