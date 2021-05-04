#Напишите программу по следующему описанию. Есть класс "Воин".
# От него создаются два экземпляра-юнита. Каждому устанавливается
# здоровье в 100 очков. В случайном порядке они бьют друг друга.
# Тот, кто бьет, здоровья не теряет. У того, кого бьют, оно
# уменьшается на 20 очков от одного удара. После каждого удара надо
# выводить сообщение, какой юнит атаковал, и сколько у противника осталось
# здоровья. Как только у кого-то заканчивается ресурс здоровья, программа
# завершается сообщением о том, кто одержал победу.
import random


class Warior:
    health_level = 100
    def __init__(self, health_level = health_level):
        self.health_level = health_level

Player_1 = Warior()
Player_2 = Warior()
for _ in range(Warior.health_level):
    a = random.randint(1, 2)
    if a == 1:
        Player_2.health_level -= 20
        print('Удар сделал Player_1.', 'У Player_2 осталось', Player_2.health_level, 'здоровья')
    else:
        Player_1.health_level -= 20
        print('Удар сделал Player_2.', 'У Player_1 осталось', Player_1.health_level, 'здоровья')
    if Player_1.health_level == 0 or Player_2.health_level == 0:
        break

