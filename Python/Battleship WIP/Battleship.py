# Battleship

import re
import time

# TODO:
# Change carrier/ship input to a function
# add player inputs for all five ships x 2 players
# Code Gameplay
"""
5 ships:
5 long (Carrier)
4 long (Battleship)
3 long (Cruiser)
3 long (Submarine)
2 long (Destroyer)
"""
ShipCoord = re.compile(r'\s*\(?\s*(\d)\s*,\s*(\d)\)?')
#Player 1's grid and Ships
Player1Name = input("Player 1, what is your name? ")
battleGrid1 = [["_" for x in range(10)] for x in range(10)]
battleGroup1 = {}
OpGrid1 = [["_" for x in range(10)] for x in range(10)]
#Player 2's Grid and Ships
Player2Name = input("Player 2, what is your name? ")
battleGrid2 = [["_" for x in range(10)] for x in range(10)]
battleGroup2 = {}
OpGrid2 = [["_" for x in range(10)] for x in range(10)]


def printGrid(playerGrid):
	print("	 ", end="")
	for j in range(0, len(playerGrid)):
		print(j, end="	")
	print("", end="\n")
	for i, k in enumerate(playerGrid):
		print(str(i) + ": " + str(k))


def placeShip(Player, playerGrid, Name, Size):
	ShipCoords = []
	placedShip = False
	while not placedShip:
		print(str(Player) + "'s Grid:")
		printGrid(playerGrid)
		print("Placing " + str(Name) + " (" + str(Size) + " spaces)")
		ShipPlacement = input("Input top or leftmost coordinate of " +
							  str(Name) + " (x,y): ")
		try:
			ShipPlacement = ShipCoord.match(ShipPlacement)
			ShipX = int(ShipPlacement.group(1))
			ShipY = int(ShipPlacement.group(2))
			upVdown = input("Place " + str(Name) +
							" horizontally or vertically? (h/v): ")
			upVdown = upVdown.replace(" ", "")
			if upVdown == "h":
				clear = True
				for x in range(Size):
					if playerGrid[ShipY][ShipX + x] != "_":
						clear = False
						print("Invalid placement, This " + str(Name) +
							  " is encroaching on another ship, try again")
						placedShip = False
				if clear:
					for x in range(Size):
						if playerGrid[ShipY][ShipX + x] == "_":
							playerGrid[ShipY][ShipX + x] = "S"
							ShipCoords.append([[ShipY, ShipX + x], "Intact"])
							placedShip = True
			if upVdown == "v":
				clear = True
				for x in range(Size):
					if playerGrid[ShipY + x][ShipX] != "_":
						clear = False
						print("Invalid placement, This " + str(Name) +
							  " is encroaching on another ship, try again")
						placedShip = False
				if clear:
					for x in range(Size):
						if playerGrid[ShipY + x][ShipX] == "_":
							playerGrid[ShipY + x][ShipX] = "S"
							ShipCoords.append([[ShipX, ShipY + x], "Intact"])
							placedShip = True
		except Exception as E:
			print("something went wrong: " + str(E))
			placedShip = False
	return ShipCoords


def SwitchPlayer(PlayerName):
	print("Switching to player " + str(PlayerName))
	for i in range(5, -1, -1):
		print(str(i) + " Seconds")
		time.sleep(1)
	for i in range(0, 50):
		print()


def playTurn(PlayerName, BattleGrid, OpGrid, OpBoat, OpGroup):
	hit = True
	while hit:
		fired = False
		print(str(PlayerName) + "'s Turn")
		print(str(PlayerName) + "'s Boats:")
		printGrid(BattleGrid)
		print("Opponent's Boats:")
		ShipX = 0
		ShipY = 0
		while not fired:
			printGrid(OpGrid)
			Target = input("Where do you want to fire? (x,y): ")
			try:
				Target = ShipCoord.match(Target)
				ShipX = int(Target.group(1))
				ShipY = int(Target.group(2))
			except Exception as E:
				print("something went wrong: " + str(E))
				fired = False
			if OpGrid[ShipY][ShipX] == "S" or OpGrid[ShipY][ShipX] == "_":
				if OpBoat[ShipY][ShipX] == "S":
					print("hit!")
					OpBoat[ShipY][ShipX] == "B"
					OpGrid[ShipY][ShipX] == "B"
					for i in OpGroup.Key():
						for j in OpGroup[i]:
							if j[0] == [ShipY, ShipX]:
								j[1] = "Burning"
					broken = True
					for j in OpGroup[i]:
						if j[1] == "Intact":
							broken = False
					if broken:
						for j in OpGroup[i]:
							j[1] = "Sunk"
							shipY = j[0][0]
							shipX = j[0][1]
							OpGrid[shipY][shipX] = "X"
							OpBoat[shipY][shipX] = "X"
				if OpBoat[ShipY][ShipX] == "_":
					print("Miss!")
					hit = False
					OpBoat[ShipY][ShipX] = "?"
					OpGrid[ShipY][ShipX] = "W"
			else:
				hit = True
				print("You Have already hit that!")


#Player 1 ship setup
print(str(Player1Name) + ", place your ships")
battleGroup1["Carrier"] = placeShip(Player1Name, battleGrid1, "Carrier", 5)
battleGroup1["Battleship"] = placeShip(Player1Name, battleGrid1, "Battleship", 4)
battleGroup1["Cruiser"] = placeShip(Player1Name, battleGrid1, "Cruiser", 3)
battleGroup1["Submarine"] = placeShip(Player1Name, battleGrid1, "Submarine", 3)
battleGroup1["Destroyer"] = placeShip(Player1Name, battleGrid1, "Destroyer", 2)
printGrid(battleGrid1)
SwitchPlayer(Player2Name)
#Player 2 ship setup
print("Player 2, place your ships")
battleGroup2["Carrier"] = placeShip(Player2Name, battleGrid2, "Carrier", 5)
battleGroup2["Battleship"] = placeShip(Player2Name, battleGrid2, "Battleship", 4)
battleGroup2["Cruiser"] = placeShip(Player2Name, battleGrid2, "Cruiser", 3)
battleGroup2["Submarine"] = placeShip(Player2Name, battleGrid2, "Submarine", 3)
battleGroup2["Destroyer"] = placeShip(Player2Name, battleGrid2, "Destroyer", 2)
printGrid(battleGrid2)
