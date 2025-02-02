extends Node

var score = 0

func add_point():
	score+=1
	%"Coins Display".text = str(score) + " Coins Collected"
	%CoinHud.text = str(score)
