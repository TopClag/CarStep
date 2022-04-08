from cProfile import run


class Car:
    def __init__(self):
        self.maxspeed = 290
        self.run = 30000
        self.engine1 = 'High'
        self.quality = 'middle'
        self.width = 1500
        self.height = 500

    def engine(self):
        print('Car engining')

    def move(self):
        print('Car moving')
    
    def stop(self):
        print('Car stoped')

    def race(self):
        self.run += 1

my_car = Car()

my_car.race()
my_car.engine()
my_car.move()
my_car.stop()
