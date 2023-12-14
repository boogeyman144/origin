import random

class RockPaperScissors:
    def __init__(self):
        self.results_file = "results.txt"
        self.wins = 0
        self.losses = 0
        self.load_results()

    def load_results(self):
        try:
            with open(self.results_file, "r") as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    parts = last_line.split(", ")
                    for part in parts:
                        if "Победы" in part:
                            self.wins = int(part.split(": ")[1])
                        elif "Поражения" in part:
                            self.losses = int(part.split(": ")[1])
        except FileNotFoundError:
            pass

    def play(self):
        while True:
            user_choice = input("Выбери камень, ножницы или бумагу (для выхода введи 'exit'): ").lower()

            if user_choice == "exit":
                print("Спасибо за игру!")
                break

            if user_choice in ["камень", "ножницы", "бумага"]:
                computer_choice = self.computer_strategy(user_choice)
                result = self.evaluate_choices(user_choice, computer_choice)
                if result == "Ты выиграл!":
                    self.wins += 1
                elif result == "Компьютер выиграл!":
                    self.losses += 1
                print(f"Выбор компьютера: {computer_choice}")
                print(result)
                self.record_result()
            else:
                print("Некорректный выбор. Попробуй еще раз!")

    def evaluate_choices(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Ничья!"
        elif (user_choice == "камень" and computer_choice == "ножницы") or \
             (user_choice == "ножницы" and computer_choice == "бумага") or \
             (user_choice == "бумага" and computer_choice == "камень"):
            return "Ты выиграл!"
        else:
            return "Компьютер выиграл!"

    def computer_strategy(self, user_choice):
        player_win_percentage = (self.wins / (self.wins + self.losses)) * 100 if self.wins + self.losses > 0 else 0

        if 40 < player_win_percentage < 60:
            return random.choice(["камень", "ножницы", "бумага"])
        elif player_win_percentage >= 60:
            return self.winning_move(user_choice)
        else:
            return self.losing_move(user_choice)

    def winning_move(self, user_choice):
        if user_choice == "камень":
            return "бумага"
        elif user_choice == "ножницы":
            return "камень"
        else:
            return "ножницы"

    def losing_move(self, user_choice):
        if user_choice == "камень":
            return "ножницы"
        elif user_choice == "ножницы":
            return "бумага"
        else:
            return "камень"

    def record_result(self):
        with open(self.results_file, "w") as file:
            file.write(f"Победы: {self.wins}, Поражения: {self.losses}")

game = RockPaperScissors()
game.play()