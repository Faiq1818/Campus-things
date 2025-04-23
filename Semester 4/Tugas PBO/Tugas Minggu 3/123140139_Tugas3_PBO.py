# Nama: Faiq Ghozy Erlangga
# NIM: 123140139
# Kelas: PBO RB
# Tugas: Minggu 3

class Pedang:
    def __init__(self, nama):
        self.nama = nama
        self.base_attack = 10
        self.base_HP = 50
    
    def sharpness_enhance(self):
        self.nama = self.nama + " +1"
        self.base_attack += 5
    
    def reinforcement_enhance(self):
        self.base_HP += 30
        self.nama = "Reinforced " + self.nama

    def attack_buff(self):
        self.nama = "Bloodlust " + self.nama 
        self.base_attack += 3

    def magic_buff(self):
        self.nama = "Magical " + self.nama 
        self.base_attack += 3

    def show_stats(self):
        print("=" * 30)
        print(f"Nama Pedang: {self.nama}")
        print(f"Serangan: {self.base_attack}")
        print(f"HP: {self.base_HP}")
        print("=" * 30)


    def show_bos_fight_winning_percentages(self):
        if(self.base_attack < 20 and self.base_HP < 70):
            print("Persentase kemenangan melawan boss adalah 50%")
        else:
            print("Persentase kemenangan melawan boss adalah 100%")

if __name__ == "__main__":
    pedang1 = Pedang("Excalibur")
    pedang1.show_stats()
    pedang1.show_bos_fight_winning_percentages()
    pedang1.sharpness_enhance()
    pedang1.reinforcement_enhance()
    pedang1.attack_buff()
    pedang1.magic_buff()
    pedang1.show_stats()
    pedang1.show_bos_fight_winning_percentages()
    