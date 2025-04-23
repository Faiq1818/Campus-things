import random

class Mine_Sweeper:
    def __init__(self):
        self.Mine_Array = [["?", "?", "?"], ["?", "?", "?"], ["?", "?", "?"]]
        self.Bomb_Row = 0
        self.Bomb_Column = 0
        self.Bomb_Founded = False

    def Show_Board(self):
        print("=========================================")
        print(f"{self.Mine_Array[0][0]} {self.Mine_Array[0][1]} {self.Mine_Array[0][2]}")
        print(f"{self.Mine_Array[1][0]} {self.Mine_Array[1][1]} {self.Mine_Array[1][2]}")
        print(f"{self.Mine_Array[2][0]} {self.Mine_Array[2][1]} {self.Mine_Array[2][2]}")
        print("=========================================")

    def Random_Bomb(self):
        BombPlaceRow = random.randrange(0, 3)
        BombPlaceColumn = random.randrange(0, 3)
        for i in range(0, 3):
            if i == BombPlaceRow:
                for j in range(0, 3):
                    if j == BombPlaceColumn:
                        self.Bomb_Row = i
                        self.Bomb_Column = j
                        

    def Choose_in_Board(self):
        row = int(input("Enter row (0-2): "))
        column = int(input("Enter column (0-2): "))

        if row == self.Bomb_Row and column == self.Bomb_Column:
            print("Yikes, you found the bomb. The end :(")
            self.Mine_Array[row][column] = "X"
            self.Bomb_Founded = True
        else:
            print("Well, there is no bomb here. Congrats!")
            self.Mine_Array[row][column] = "0"

    def Play(self):
        Stop = False
        iteration = 0
        self.Random_Bomb()
        self.Show_Board()
        while Stop == False:
            self.Choose_in_Board()
            self.Show_Board()
            iteration += 1
            if self.Bomb_Founded == True:
                break

            if iteration == 8:
                print("Congrats you win!")

            


                        
ayomain = Mine_Sweeper()
ayomain.Play()



