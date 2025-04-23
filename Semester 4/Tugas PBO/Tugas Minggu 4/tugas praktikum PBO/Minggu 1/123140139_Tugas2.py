# Nama: Faiq Ghozy Erlangga
# NIM: 123140139
# Kelas: Praktikum PBO Robot
# Tugas: 2

import copy #mengimport modul copy dan random untuk digunakan di kode
import random

class Robot:
    def __init__(self, nama, attack, hp):#class memiliki 3 atribut yaitu nama, jumlah attack dan jumlah hp
        self.nama = nama
        self.attack = attack
        self.hp = hp

    def attack_enemy(self, target, multiplication):#method attack_enemy, yang berguna untuk mengattack enemy
        damage = self.attack * multiplication
        target.hp -= damage

        print(f"{self.nama} menyerang dengan damage {damage:.2f}!")
        print(f"HP {target.nama}: {target.hp:.2f}")
        print("")


def gamestart(player1z, player2z): #fungsi untuk pertarungan
    player1 = copy.deepcopy(player1z)
    player2 = copy.deepcopy(player2z)
    x = False
    defense_multiplier = 1
    isdefense = False

    while not x:
        print("---- 1. Attack ---- 2. Defense ---- 3. Exit ----")
        n = input("Pilih aksi: ")

        n = int(n)
        print("")
        multiplication = random.uniform(0.7, 2)

        if n == 1:
            player1.attack_enemy(player2, defense_multiplier)
            defense_multiplier = 1 #ini untuk mereset multiplication setelah digunakan sekali
        elif n == 2:
            defense_multiplier = multiplication #jika memilih 2, maka multiplier akan aktif
            print(f"{player1.nama} mendefense! Serangan berikutnya ({multiplication:.2f}x damage).")
            isdefense = True
        elif n == 3:
            x = True #jika memilih 3, maka pertarungan akan langsung berakhir karena di break
            break
        else:
            print("Pilihan tidak valid!")
            continue
        
        if isdefense:
            player2.attack_enemy(player1, 0.5) #musuh menyerang
        else: 
            player2.attack_enemy(player1, 1)
        if player1.hp <= 0: #jika hp player kurang dari 0 maka player kalah, jika hp musuh kurang dari 0 maka player menang
            print(f"{player1.nama} kalah!")
            break
        elif player2.hp <= 0:
            print(f"{player2.nama} kalah!")
            break


player = Robot("Player", 50, 100) #menginisiasi objek
enemy = Robot("Enemy", 45, 110)

gamestart(player, enemy) #memulai pertarungan
