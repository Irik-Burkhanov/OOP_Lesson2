class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина марки {self.name} поехала со скоростью {self.speed} км/ч')

    def stop(self):
        print(f'Машина марки {self.name} {self.color} цвета остановилась')

    def turn(self, direction):
        print(f'Машина марки {self.name} повернула {direction}')

class TownCar(Car):
    pass
class SportCar(Car):
    pass
class WorkCar(Car):
    pass
class PoliceCar(Car):
    pass

car1 = TownCar(80, 'green', 'volvo', False)
car1.turn('влево')

car2 = SportCar(300, 'red', 'Ferrari', False)
car2.go()