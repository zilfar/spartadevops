print("\nQ1a\n")


# Q1a: Create a class which of a country (include continent, climate, language etc in the inputs)

# A1a:
class Country:
    def __init__(self, continent, climate, language):
        self.__continent = continent
        self.climate = climate
        self._language = language

    def __str__(self):
        return f"This country is in the continent {self.__continent}, has a {self.climate} " \
               f"climate, and speaks the national language {self._language}."


brazil = Country('South America', 'tropical', 'Portuguese')

print("\nQ1b\n")


# Q1b: Create a subclass of a city which inherits from the country class

# A1b:
class City(Country):
    def __init__(self, continent, climate, language):
        super().__init__(continent, climate, language)
        self.__continent = continent
        self.climate = climate
        self._language = language

    def __str__(self):
        return f"This City is in the continent {self.__continent}, has a {self.climate} " \
               f"climate, and speaks the national language {self._language}."


london = City("Europe", "temperate", "English")

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: Using the predefined class and is_prime method below, loop through list_of_numbers and create
# a list of primes from that list
list_of_numbers = [1, 12, 44, 53, 6, 3, 6545, 76, 32, 345, 22, 17, 19, 223, 156]


class Number:
    def __init__(self, integer):
        self.integer = integer

    def is_prime(self):
        if self.integer >= 2:
            for x in range(2, self.integer):
                if self.integer % x == 0:
                    return False
            return True
        else:
            return False

    def divisible_by_n(self, n):
        if self.integer % n == 0:
            return True
        else:
            return False

# A2a:
p = []
for number in list_of_numbers:
    if Number(number).is_prime(): p.append(number)
print(p)

print("\nQ2b\n")
# Q2b: Now create a list of numbers from list_of_numbers that are divisible
# by both 3 and 4 using the divisible_by_n method above

# A2b:ʕ •ᴥ•ʔ
d = []
for number in list_of_numbers:
    if Number(number).divisible_by_n(3) and Number(number).divisible_by_n(4): d.append(number)
print(d)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Fix the following class and subclass (uncomment by selecting all rows and pressing CTRL + /)
# A3a:

class Boss(object):
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        return self.attitude

    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face


class GoodBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        super().__init__(name, attitude, behaviour, face)
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def encourage(self):
        print(f"The team cheers for {self.name}, starts shouting awesome slogans then gets back to work.")


niceBoss = GoodBoss('jason', 'happy', 'chilling', 'stern')

niceBoss.encourage()
print(niceBoss.get_behaviour(), niceBoss.get_attitude(), niceBoss.get_face())

# -------------------------------------------------------------------------------------- #
