import random

class Hangman:
    def __init__(self):
        self.words = [
            'algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
            'encryption', 'framework', 'function', 'garbage', 'hash', 'index', 'iterator',
            'javascript', 'json', 'library', 'loop', 'namespace', 'object', 'operator',
            'overload', 'polymorphism', 'queue', 'recursion', 'serialization', 'stack',
            'template', 'variable', 'virtual', 'web', 'xml', 'yaml', 'zip'
        ]
        self.stages = ["""
                ------
                |    |
                |
                |
                |
                |
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |
                |
                |
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |    |
                |    |
                |
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |    |
                |    |
                |   /
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |    |
                |    |
                |   / \\
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |  --|
                |    |
                |   / \\
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |  --|--
                |    |
                |   / \\
                |
            ------------
        """]

    def Play(self):
        randomWord = random.choice(self.words)
        maxAttempts = len(self.stages) - 1
        guessed = ['_'] * len(randomWord)
        attempts = 0

        while attempts < maxAttempts and "_" in guessed:
            print(self.stages[attempts])
            print("Guessed: " + ' '.join(guessed))
            guess = input().lower()

            if guess in guessed:
                print("You already guessed that letter.")
                continue

            if guess in randomWord:
                for i, letter in enumerate(randomWord):
                    if letter == guess:
                        guessed[i] = guess
            else:
                attempts += 1

        if '_' not in guessed:
            print("You win, The word is:", randomWord)
        else:
            print(self.stages[attempts])
            print("Game over! The word is:", randomWord)


ayoMain = Hangman()
ayoMain.Play()