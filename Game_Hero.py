#Разработайте программу по следующему описанию.
# В некой игре-стратегии есть солдаты и герои. У всех есть
# свойство, содержащее уникальный номер объекта, и свойство,
# в котором хранится принадлежность команде. У солдат есть
# метод "иду за героем", который в качестве аргумента принимает
# объект типа "герой". У героев есть метод увеличения собственного уровня.
# В основной ветке программы создается по одному герою для каждой
# команды. В цикле генерируются объекты-солдаты. Их принадлежность
# команде определяется случайно. Солдаты разных команд добавляются
# в разные списки.
# Измеряется длина списков солдат противоборствующих команд и выводится
# на экран. У героя, принадлежащего команде с более длинным списком,
# увеличивается уровень. Отправьте одного из солдат первого героя
# следовать за ним. Выведите на экран идентификационные номера этих двух юнитов.
import random

class Soldiers:

    def __init__(self, id_person, team):
        self.id_person = id_person
        self.team = team

    def go (self, hero):
        print("Solder", self.id_person, "follow the Hero", hero.id_person)

class Hero(Soldiers):
    def __init__(self,id_person, team, level = 0):
        self.level = level
        super().__init__(id_person, team)

    def lvl(self):
        self.level += 1
        print("Hero", self.id_person, "up level")
        return self.level

hero1 = Hero(1, 1, 0)
hero2 = Hero(2, 2, 0)
team_1 = []
team_2 = []
s = int(input('Введите колличество солдат: '))
ss = s+3
for elem in range(3,ss):
    soldiers = Soldiers(elem, random.randint(1, 2))
    if soldiers.team == 1:
        team_1.append(soldiers)
    else:
        team_2.append(soldiers)

print("Emount of solders for Hero", hero1.id_person, "is", len(team_1),
      "\nEmount of solders for Hero", hero2.id_person, "is", len(team_2))

if len(team_1) > len(team_2):
    hero1.lvl()
    q = random.choice(team_1)
    q.go(hero1)
    print("Hero ID: ", hero1.id_person, ", Solders ID: ", soldiers.id_person)
if len(team_2) > len(team_1):
    hero2.lvl()
    q = random.choice(team_2)
    q.go(hero2)
    print("Hero ID: ", hero1.id_person, ", Solders ID: ", soldiers.id_person)
if len(team_1) == len(team_2):
    print("Draw")
