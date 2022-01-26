# Complete = False
#
# while not Complete:
#     print("I'd like to know your name, age and your favourite colour!\n")
#     firstAnswer = input("Please tell me your name, first of all.\n")
#     if firstAnswer.isalpha():
#         print("That's a nice name!")
#         secondAnswer = input("Could you tell me your age now, please? Only numbers now :)\n")
#         if not secondAnswer.isalpha() and 120 > int(secondAnswer) >= 0:
#             print("Great!")
#             finalAnswer = input("This is the final question, what is your favourite colour?\n")
#             if finalAnswer.isalpha():
#                 print("Fantastic!\n")
#                 print("So, your name is " + firstAnswer.capitalize() + ", you're " + secondAnswer + " years old and your favourite colour is " + finalAnswer + "! Nice to meet you :)")
#                 Complete = True
#             else:
#                 print("Your favourite colour can't be a number! Use your words! Let's start over.\n\n")
#         else:
#             print("Either your answer is ridiculous or wasn't numeric. Let's start from scratch.\n")
#     else:
#         print("please try again. Names have only alphabetic letters in them!\n")

#
# prompt_user = True
# age = None
# while prompt_user:
#     age = input("What is your age?\n")
#     if age.isdigit():
#
#         if int(age) == 0:
#             print(f"Double your age is {int(age) * 2} ... You're zero years old? Try again.")
#         if 0 < int(age) < 18:
#             print(f"Double your age is {int(age) * 2} ... that means you're a little bit young.")
#             prompt_user = False
#         elif int(age) < 100:
#             print(f"Double your age is {int(age) * 2}")
#             prompt_user = False
#         elif int(age) < 120:
#             print(f"Double your age is {int(age) * 2} ... A ripe old age.")
#             prompt_user = False
#         elif int(age) >= 120:
#             print(f"Double your age is {int(age) * 2} ... Maybe a bit too old. Try again.")
#
#     else:
#         print("Please provide a sensible age in digits.")



class Car:

    # max_speed, current speed

    def __init__(self, current_speed, max_speed, cartype=None, canMassage = None, companyID = None):
        self.current_speed = current_speed
        self.max_speed = max_speed
        self.__cartype = cartype
        self.__companyID = companyID
        self.canMassage = canMassage

    def accelerate(self, speed_increase):
        self.current_speed = min(self.max_speed, self.current_speed + abs(speed_increase))

    def brake(self, speed_decrease):
        self.current_speed = max(0, self.current_speed - abs(speed_decrease))

    def __repr__(self):
        return f"Car(current_speed={self.current_speed}, max_speed={self.max_speed}, cartype={str(self.__cartype)})"

    def __str__(self):
        return f"This is a car currently traveling at {self.current_speed:.2f} mph with a maximum speed of " \
               f"{self.max_speed:.2f} mph and the assigned car type is {str(self.__cartype)}. "

    def __format__(self, format_spec):
        if format_spec == "km":
            return f"This is a car currently traveling at {self.current_speed * 8 / 5:.2f} kmh with a maximum " \
                   f"speed of {self.max_speed * 8 / 5:.2f} kmh and the assigned car type is {str(self.__cartype)}."
        else:
            return self.__str__()


class Audi(Car):
    def __init__(self, current_speed, max_speed):
        super().__init__(current_speed, max_speed, "audi", True, "123353498AUDI")


if __name__ == "__main__":
    print('this isn\'t an imported module')
    car1 = Car(140, 260, "McClaren")
    print(car1.current_speed)
    car1.accelerate(400)
    print(car1.current_speed)
    car1.accelerate(20)
    print(car1.current_speed)
    car1.brake(40)
    print(car1.current_speed)
    car1.brake(260)
    print(car1.current_speed)
    print(repr(car1))
    print(car1)
    print(f"{car1:kdm}")

#
# def add(int1: int, int2: int) -> int:
#     return int(int1) + int(int2)
#
#
# def subtract(int1: int, int2: int) -> int:
#     return int(int1) - int(int2)
#
#
# def multiply(int1: int, int2: int) -> int:
#     return int(int1) * int(int2)
#
#
# def divide(int1: int, int2: int) -> float:
#     return int(int1) / int(int2)

class Human:
    def __init__(self, age, gender, social_credits, money, criminal_record=False):
        self.age = age
        self.gender = gender.lower()
        self.social_credits = social_credits
        self.money = money
        self.criminal_record = criminal_record

    def human_worth(self):
        multiplier = 1
        if self.gender == "m":
            multiplier += 1
        worth = multiplier * (self.money) * (self.social_credits) * (.0001 / (self.age + 10))
        if worth == 0 or self.criminal_record:
            return "doesn't deserve to be alive"
        elif 0 < worth < 100:
            return "has potential, but is on the edge"
        else:
            return "outstanding citizen"

if __name__ == "__main__":
    jay = Human(14, 'm', 340, 5000)
    print(jay.human_worth())
    delinquent = Human(28, 'f', 800, 14000)
    print(delinquent.human_worth())
    johnxina = Human(44, 'm', 1430, 80540)
    print(johnxina.human_worth())
    chad = Human(64, 'm', 5310, 594230, True)
    print(chad.human_worth())