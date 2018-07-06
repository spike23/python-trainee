

# пример ООП
class Hero(object):
    def __init__(self, name, level, race):
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        description = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is: " +
                       str(self.health)).title()
        print(description)

    def level_up(self):
        self.level += 1

    def move(self):
        print("Hero " + self.name + " start moving.")

    def set_health(self, new_halth):
        self.health = new_halth


hero_1 = Hero("Tor", 4, "Human.")
hero_2 = Hero("Leo", 5, "Turtle.")


class SuperHero(Hero):
    def __init__(self, name, level, race, magic_level):
        super().__init__(name, level, race)
        self.magiclevel = magic_level
        self.magic = 100

    def make_magic(self):
        self.magic -= 10

    def show_hero(self):
        description = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is: " +
                       str(self.health) + " Magic is: " + str(self.magic)).title()
        print(description)


hero_3 = SuperHero("Gendalf", 10, "Wizard.", 90)


if __name__ == '__main__':
    hero_1.show_hero()
    hero_2.move()
    hero_2.show_hero()
    hero_2.level_up()
    hero_2.show_hero()
    hero_1.set_health(80)
    hero_1.show_hero()
    hero_3.show_hero()
    hero_3.make_magic()
    hero_3.show_hero()

