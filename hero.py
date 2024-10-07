import random


class SuperHero:
    people = "people"

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def sayname(self):
        print(f"Его имя {self.name}.")

    def health_points_x2(self):
        self.health_points = self.health_points * 2

    def __str__(self):
        return f"Мое прозвище - {self.nickname}. Моя суперсила - {self.superpower}. Мои хп: {self.health_points}."

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Брюс Уейн", "Бэтмен", "ахаха", 250, "Я - Бэтмен")
hero.sayname()
hero.health_points_x2()
print(hero)


class EarthHero(SuperHero):
    fly = False

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, weapon):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.weapon = weapon

    def mutation(self):
        super().health_points_x2()
        self.health_points *= self.health_points
        self.fly = True

    def phrase(self):
        print("True in the True_Phrase")

    def __str__(self):
        return f"{SuperHero.__str__(self)} Урон: {self.damage}"


ehero = EarthHero("Брюс Уейн", "Бэтмен", "полёт", 250, "Я - Бэтмен", 300, True)
ehero.mutation()
print(ehero)


class CosmicHero(SuperHero):
    fly = False

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, magic):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.magic = magic

    def crit2(self):
        Villain.crit(self)

    def __str__(self):
        return f"{SuperHero.__str__(self)} Урон: {self.damage}"


class Villain(EarthHero):
    people = "monster"

    def gen_x(self):
        ...

    def crit(self):
        r = random.randint(1,2)
        self.damage = self.damage ** r




print(Villain.mro())
villain = Villain("Феникс", "Джокер", "ахаха", 150, "АХАХА", 100, False)
villain.crit()
print(villain)
cosmic = CosmicHero("Кевин", "Супермен", "Суперсилы", 100000, "Справедливость", 100000, False)
cosmic.crit2()
print(cosmic)

# 10 молодец