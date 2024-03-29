class Player:

 def __init__(self, name):
        self.name = name
        self.total_twos = 0
        self.total_threes = 0
        self.total_floaters = 0
        self.total_free_throws = 0
        self.total_shots = 0

 def record_results(self, twos, threes, floaters, free_throws):
        self.total_twos += twos
        self.total_threes += threes
        self.total_floaters += floaters
        self.total_free_throws += free_throws
        self.total_shots += (twos + threes + floaters + free_throws)

 def print_results(self, week):
        accuracy_percentage = (self.total_shots / (week * 250)) * 100
        print(f"\n{self.name}'s Results After Workout {week}:")
        print(f"Total 2p shots: {self.total_twos} / {week*100} ({((self.total_twos/(week*100))*100):.1f})")
        print(f"Total 3p shots: {self.total_threes} / {week*100} ({((self.total_threes/(week*100))*100):.1f})")
        print(f"Total floater shots: {self.total_floaters} / {week*30} ({((self.total_floaters/(week*30))*100):.1f})")
        print(f"Total free throws: {self.total_free_throws} / {week*20} ({((self.total_free_throws/(week*20))*100):.1f})")
        print(f"Total shots and accuracy % this week was {self.total_shots} / {week * 250} ({accuracy_percentage:.1f}%)")
        print("")

def main():
    players = []

    while True:
        player_name = input("Enter player's name (type 'Done' to finish): ")
        if player_name.lower() == "done":
            break
        player = Player(player_name)
        players.append(player)

    workouts = int(input("How many workouts you've done?: "))
    print("")

    for workout in range(1, workouts + 1):
        print(f"Workout {workout}:")

        for player in players:
            print(f"{player.name}:")
            twos = int(input("Fill 2p shots here (? / 100): "))
            threes = int(input("Fill 3p shots here (? / 100): "))
            floaters = int(input("Fill floater shots here (? / 30): "))
            free_throws = int(input("Fill free throws here (? / 20): "))

            player.record_results(twos, threes, floaters, free_throws)

        print(f"\nResults After Workout {workout}:\n")
        for player in players:
            player.print_results(workout)

if __name__ == "__main__":
    main()