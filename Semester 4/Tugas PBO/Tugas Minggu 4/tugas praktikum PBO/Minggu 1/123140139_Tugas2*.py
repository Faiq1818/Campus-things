import copy
import random

class Robot:
    def __init__(self, nama, attack, hp):
        self.nama = nama
        self.attack = attack
        self.hp = hp

    def attack_enemy(self, target, multiplication):
        if multiplication == 0:
            target.hp = target.hp - self.attack
        else:
            target.hp = target.hp - self.attack * 0.5

        print(f"{self.nama} menyerang!")
        print(f"hp {target.nama} : {target.hp}")
        print("")


def gamestart(player1z, player2z):
    player1 = copy.deepcopy(player1z)
    player2 = copy.deepcopy(player2z)
    x = False
    while not x:
        print("---- 1. attack ---- 2. defense ---- 3. exit ----")
        print("Pilih aksi: ")
        n = int(input())
        print("")
        m = False
        multiplication = random.uniform(0.7, 2)

        if n == 1:
            player1.attack_enemy(player2, multiplication)
        elif n == 2:
            m = True
        elif n == 3:
            x = True

        if m:
            print(
                f"{player1.nama} mendefense, mendapatkan multiplication sebesar {multiplication} untuk serangan berikutnya"
            )
            print("")
            player2.attack_enemy(player1, multiplication)
        else:
            multiplication = 0
            player2.attack_enemy(player1, 0)


player = Robot("player", 50, 100)
enemy = Robot("enemy", 45, 110)

gamestart(player, enemy)
