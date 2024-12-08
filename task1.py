import math

class calculator:
    a=0
    b=0

    def write_a(self):
        while 1:
            try:
                a=int(input("Введите 1 число\n"))
                self.a=a
                return a

            except Exception as e:
                print("Ошибка, введите число")


    def write_b(self):
        while 1:
            try:
                b = int(input("Введите 2 число\n"))
                self.b = b
                return b
            except Exception as e:
                print("Ошибка, введите число")



    def devide(self,a,b):
        try:
            num=a/b
            return num
        except ZeroDivisionError as e:
            return "Ошибка, деление на ноль"

    def rest_from_devide(self,a,b):
        try:
            num=a%b
            return num
        except ZeroDivisionError as e:
            return "Ошибка, деление на ноль"

    def full_devide(self, a, b):
        try:
            num = a // b
            return num
        except ZeroDivisionError as e:
            return "Ошибка, деление на ноль"
    def multiple(self,a,b):
        return a*b
    def summ(self,a,b):
        return a+b
    def minus(self,a,b):
        return a-b
    def num_pow(self,a,b):
        return math.pow(a,b)
    def sqrt(self,a):
        try:
            num=math.sqrt(a)
            return num
        except Exception as e:
            return "Ошибка, отрицательное число под корнем"
    def log(self,a,b):
        try:
            num = math.log(b,a)
            return num
        except Exception as e:
            return "Ошибка, неверные параметры логарифма"


calc=calculator()
print(calc.summ(calc.write_a(),calc.write_b()))
print(calc.minus(calc.write_a(),calc.write_b()))
print(calc.multiple(calc.write_a(),calc.write_b()))
print(calc.devide(calc.write_a(),calc.write_b()))
print(calc.full_devide(calc.write_a(),calc.write_b()))
print(calc.rest_from_devide(calc.write_a(),calc.write_b()))
print(calc.num_pow(calc.write_a(),calc.write_b()))
print(calc.sqrt(calc.write_a()))
print(calc.log(calc.write_a(),calc.write_b()))