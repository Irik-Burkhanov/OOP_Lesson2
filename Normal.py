import random
from random import randint

class Person:
    def __init__(self, name):
        self.name = name
        self.health = randint(100, 200)
        self.armor = randint(50,200)
        self.damage = randint(50, 150)

    def info(self):
        print(
        f'{self.name} health: {round(self.health, 2)}',
        f'damage {self.damage}',
        f'armor {self.armor}'
        )

    def _attack(self, enemy_health, armor_enemy):
        enemy_health -= self._damage_calculation(armor_enemy)
        return enemy_health

    def _damage_calculation(self, armor_enemy):
        dmg = round(armor_enemy/self.damage, 1)
        return dmg

    def battle(self, enemy):
        enemy.health = self._attack(enemy.health, enemy.armor)

class Player(Person):
    pass
class Enemy(Person):
    pass



player1 = Player('player1')
enemy1 = Enemy('enemy1')
round_battle = 0

while player1.health > 0 and enemy1.health > 0:
    player1.info()
    enemy1.info()
    round_battle += 1
    print(f'Раунд: {round_battle}')

    player1.battle(enemy1)
    if enemy1.health > 0:
        enemy1.battle(player1)

if player1.health <= 0 < enemy1.health:
    print(f'Выиграл игрок {enemy1.name}!')
elif enemy1.health <= 0 < player1.health:
    print(f'Выиграл игрок {player1.name}!')
else:
    print('Ничья')