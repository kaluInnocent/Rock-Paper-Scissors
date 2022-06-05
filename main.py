""" Returns a random element from the given sequence
Usage:
		import random
		my_list =	[1, 2, 3]
		print(random.choice(my_list))
		>>2
"""
import random

game = ["Paper", "Rock", "Scissors"]
player =	False
cpu = random.choice(game)
player_score = 0
cpu_score = 0
print("===================Rock, Paper, Scissors===================\n")

while True:
	player = input("Enter Paper, Rock, or Scissors to play or q to quit:  ").title()
	if player in game:
		print(f"Player({player}): CPU({cpu})\n")
		if player == cpu:
			print(f"CPU({cpu}), Player({player}), it's a tie!\n")
		elif player == "Rock":
			if cpu == "Paper":
				print(f"You lose, {cpu} covers {player}!")
				cpu_score += 1
			else:
				print(f"You win!, {player} smashes {cpu}!")
				player_score += 1
		elif player == "Paper":
			if cpu == "Scisssors":
				print(f"You lose!, {cpu} cuts {player}")
				cpu_score += 1
			else:
				print(f"You win, {player} covers {cpu}!")
		elif player == "Scissors":
			if cpu == "Rock":
				print(f"You lose, {cpu} smashes {player}!")
				cpu_score += 1
			else:
				print(f"You win, {player} cuts {cpu}!")
				player_score += 1
	elif player == "Q":
		print("Final Scores: ")
		print(f"CPU: {cpu_score}")
		print(f"Player: {player_score}")
		break
	else:
		print("Incorrect choice, try again\n")
