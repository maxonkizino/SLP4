class Car:
    speed=0
    color=""
    name=""
    is_police=False
    def go(self,speed):
        self.speed=speed
        print("car goes")
        pass

    def stop(self):
        self.speed=0
        print("car is staying")

    def turn(self,dir):
        if dir=="right":
            print("car turns right")
        elif dir=="left":
            print("car turns left")
        else:
            print("invalid option")

    def show_speed(self):
        print("car have speed: ",self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed<=60:
            print("car have speed: ",self.speed)
        else:
            print("You Exceed the limit")


class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print("car have speed: ", self.speed)
        else:
            print("You Exceed the limit")
             
class SportCar(Car):
    pass



class PoliceCar(Car):
    is_police = True
