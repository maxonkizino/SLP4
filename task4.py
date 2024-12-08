class Person:
    name=""
    def __init__(self,name):
        self.name=name

    @staticmethod
    def greet(self):
        print("Hi, I'm ",self.name)

    @classmethod
    def say(cls,name):
        cls.name=name
        pass



