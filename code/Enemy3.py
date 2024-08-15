# code/Enemy3.py

import random
from code.Enemy import Enemy
from code.Const import WIN_HEIGHT, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot


class Enemy3(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed_x = 3  # Velocidade horizontal
        self.speed_y = 2  # Velocidade vertical
        self.health = 150  # Vida específica para Enemy3

    def move(self):
        # Movimento horizontal da direita para a esquerda
        self.rect.centerx -= self.speed_x

        # Movimento vertical (sobe e desce)
        self.rect.centery += self.speed_y

        # Verifica se bate na borda superior ou inferior
        if self.rect.top <= 0:
            self.speed_y = abs(self.speed_y)  # Muda para descer com velocidade normal
        elif self.rect.bottom >= WIN_HEIGHT:
            self.speed_y = -2 * abs(self.speed_y)  # Muda para subir com o dobro da velocidade

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Enemy3Shot', position=(self.rect.centerx, self.rect.centery))
