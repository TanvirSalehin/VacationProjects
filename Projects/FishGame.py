import random
import math
import os

tot_money = 100000000

#--------Rod Prices---------
stonerod = 10000
ironrod = 80000
goldrod = 600000
#---------------------------


#--------Boat Prices--------
woodenraft = 21000
woodenboat = 110000
fishingboat = 800000
#---------------------------


#--------Bait Prices--------

#---------------------------


#--------Total Fish---------
tot_salmon = 0
tot_cod = 0
tot_squid = 0
#---------------------------


#--------Fish Prices--------
salmonprice = 3
codprice = 7
squidprice = 35
#---------------------------


#---------------------------
fishrod = "Wooden Rod"
boat = "Plastic Raft"
#---------------------------


#--------Owned Items--------
ownboats = ["Plastic Raft"]
ownrods = ["Wooden Rod"]
#---------------------------

savedonce = False

fish_data = []
boat_rod_data = []

if not os.path.isdir("FishGameData"):
	savedonce = False
	os.mkdir("FishGameData")
#	if not os.path.isdir("FishGameData/OwnBoats"):
#		os.mkdir("FishGame/OwnBoats")
#		if not os.path.isdir("FishGameData/OwnBoats/Plastic Raft.txt"):
#			os.mkdir("FishGame/OwnBoats")
#
#	if not os.path.isdir("FishGameData/OwnRods"):
#		os.mkdir("FishGame/OwnRods")
#		if not os.path.isdir("FishGameData/OwnRods/Wooden Rod.txt"):
#			os.mkdir("FishGame/OwnRods")
else:
	savedonce = True



def resize(str):
    strsplit = str.split()
    #strsplit = strsplit.pop()
    str = "".join(strsplit)
    return str


class save():
	def __init__(self):
		self.money()
		self.salmon()
		self.cod()
		self.squid()
		self.boat()
		self.rod()
		self.ownboats()
		self.ownrods()

		global savedonce
		savedonce = True

	def money(self):
		with open("FishGameData/money.txt", "w") as file:
			file.write(str(tot_money))

	def salmon(self):
		with open("FishGameData/salmon.txt", "w") as file:
			file.write(str(tot_salmon))

	def cod(self):
		with open("FishGameData/cod.txt", "w") as file:
			file.write(str(tot_cod))

	def squid(self):
		with open("FishGameData/squid.txt", "w") as file:
			file.write(str(tot_squid))
	
	def boat(self):
		with open("FishGameData/boat.txt", "w") as file:
			file.write(boat)
	
	def rod(self):
		with open("FishGameData/rod.txt", "w") as file:
			file.write(fishrod)

#	def ownboats(self):
#		for boat in ownboats:
#			boatfile = "FishGameData/OwnBoats" + str(boat) + ".txt"
#			with open(boatfile, "w") as file:
#				file.write(boat)

#	def ownrods(self):
#		for rod in ownrods:
#			rodfile = "FishGameData/OwnRods" + str(rod) + ".txt"
#			with open(rodfile, "w") as file:
#				file.write(rod)

	def ownboats(self):
		with open("FishGameData/ownboats.txt", "w") as file:
			for line in ownboats:
				file.write(line + "\n")

	def ownrods(self):
		with open("FishGameData/ownrods.txt", "w") as file:
			for line in ownrods:
				file.write(line + "\n")


class readData():
	def __init__(self):
		self.money()
		self.salmon()
		self.cod()
		self.squid()
		self.boat()
		self.rod()
		self.ownboats()
		self.ownrods()

	def money(self):
		global tot_money
		with open("FishGameData/money.txt", "r") as readfile:
			tot_money = int(readfile.read())

	def salmon(self):
		global tot_salmon
		with open("FishGameData/salmon.txt", "r") as readfile:
			tot_salmon = int(readfile.read())

	def cod(self):
		global tot_cod
		with open("FishGameData/cod.txt", "r") as readfile:
			tot_cod = int(readfile.read())
	
	def squid(self):
		global tot_squid
		with open("FishGameData/squid.txt", "r") as readfile:
			tot_squid = int(readfile.read())

	def boat(self):
		global boat
		with open("FishGameData/boat.txt", "r") as readfile:
			boat = readfile.read()

	def rod(self):
		global fishrod
		with open("FishGameData/rod.txt", "r") as readfile:
			fishrod = readfile.read()

	def ownboats(self):
		global ownboats
		ownboats.pop()
		with open("FishGameData/ownboats.txt", "r") as readfile:
			temp = readfile.readlines()
		for line in temp:
			line = line.strip()
			ownboats.append(line)

	def ownrods(self):
		global ownrods
		ownrods.pop()
		with open("FishGameData/ownrods.txt", "r") as readfile:
			temp = readfile.readlines()
		for line in temp:
			line = line.strip()
			ownrods.append(line)

#-----------------INIT---------------------
if savedonce:
	readData()
	save()



if __name__ == "__main__":
	print("Write help() and hit enter to get help.")


def help():
	pass


def catchsalmon():
	randomiser = random.randint(1,10)
	if randomiser <= 2:
		salmon = random.randint(5,9)
	elif (randomiser > 2) or (randomiser < 9):
		salmon = random.randint(10,20)
	else:
		salmon = random.randint(21,27)
	return salmon


def catchcod():
	randomiser = random.randint(1,10)
	if randomiser <= 2:
		cod = random.randint(1,3)
	elif (randomiser > 2) or (randomiser < 9):
		cod = random.randint(4,9)
	else:
		cod = random.randint(10,14)
	return cod


def catchsquid():
	randomiser = random.randint(1,10)
	if randomiser <= 2:
		squid = 1
	elif (randomiser > 2) or (randomiser < 9):
		squid = random.randint(1,3)
	else:
		squid = random.randint(3,5)
	return squid



def c():
	Salmons = catchsalmon()
	Cods = catchcod()
	Squids = catchsquid()


	#----------------------Fish Rod----------------------

	if fishrod == "Wooden Rod":
		Squids = 0

	elif fishrod == "Stone Rod":
		Salmons = math.ceil(Salmons * 1.5)
		Cods = math.ceil(Cods * 1.7)
		Squids = 0

	elif fishrod == "Iron Rod":
		Salmons = math.ceil(Salmons * 2.1)
		Cods = math.ceil(Cods * 2.8)
		Squids = math.floor(Squids * 0.4)

	elif fishrod == "Gold Rod":
		Salmons = math.ceil(Salmons * 4)
		Cods = math.ceil(Cods * 6.5)
		Squids = math.ceil(Squids * 1.5)

	#----------------------------------------------------

	#------------------------Boat------------------------

	if boat == "Plastic Raft":
		Squids = 0
		if Salmons > 30:
			Salmons = random.randint(25, 33)
		if Cods > 21:
			Cods = random.randint(18, 23)

	elif boat == "Wooden Raft":
		if Salmons > 52:
			Salmons = random.randint(43, 54)
		if Cods > 34:
			Cods = random.randint(29, 37)
		if Squids > 2:
			Squids = random.randint(1,2)

	elif boat == "Wooden Boat":
		if Salmons > 84:
			Salmons = random.randint(77, 89)
			Salmons = math.ceil(Salmons * 1.6)
		if Cods > 77:
			Cods = random.randint(70, 80)
			Cods = math.ceil(Cods * 1.8)
		if Squids > 5:
			Squids = random.randint(3,5)

	elif boat == "Fishing Boat":
		if Salmons > 84:
			#Salmons = random.randint(77, 89)
			Salmons = math.ceil(Salmons * 2.6)
		if Cods > 77:
			#Cods = random.randint(70, 80)
			Cods = math.ceil(Cods * 3.2)
		if Squids > 5:
			#Squids = random.randint(3,5)
			Squids = math.ceil(Squids * 1.8)

	#----------------------------------------------------

	#------------------------Bait------------------------

	# Write from here_

	#----------------------------------------------------


	global tot_salmon
	global tot_cod
	global tot_squid

	tot_salmon += Salmons
	tot_cod += Cods
	tot_squid += Squids

	print("Salmon         :     " , Salmons)
	print("Cod            :     " , Cods)
	if Squids != 0:
		print("Squids         :     " , Squids)


	save()

def catch():
	c()


def p():
	print("\nThis is your profile\n---------------------\n")
	print("Salmon        :     " , tot_salmon)
	print("Cod           :     " , tot_cod)
	print("Squid         :     " , tot_squid)
	print("\nMoney         :     " , tot_money)
	print("\nFishing Rod   :     " , fishrod)
	print("Boat          :     " , boat)

def profile():
	p()


def sellsalmon():
	global tot_salmon
	money = tot_salmon * salmonprice
	tot_salmon = 0 
	return money

def ssalmon():
	sellsalmon()


def sellcod():
	global tot_cod
	money = tot_cod * codprice
	tot_cod = 0
	return money

def scod():
	sellcod()


def sellsquid():
	global tot_squid
	money = tot_squid * squidprice
	tot_squid = 0
	return money







def sellall():
	salmonmoney = int(sellsalmon())
	codmoney = int(sellcod())
	squidmoney = int(sellsquid())
	totalmoney = salmonmoney + codmoney + squidmoney

	global tot_money
	tot_money += totalmoney 
	print("You've earned " , totalmoney , " dollars!")


	save()

def s():
	sellall()


def buy(Code):
	global tot_money
	global fishrod
	global boat

	#---------------------------------------------Rods----------------------------------------------

	if Code == 1:
		if "Stone Rod" in ownboats:
			print("You already own Stone Rod")
		if tot_money >= stonerod:
			tot_money -= stonerod
			fishrod = "Stone Rod"
			ownrods.append("Stone Rod")
			print("You successfully bought Stone Rod!")
		else:
			print("You dont have enough money. Stone Rod's price is " , stonerod , " Dollars")
	elif Code == 2:
		if "Iron Rod" in ownboats:
			print("You already own Iron Rod")
		if tot_money >= ironrod:
			tot_money -= ironrod
			fishrod = "Iron Rod"
			ownrods.append("Iron Rod")
			print("You successfully bought Iron Rod!")
		else:
			print("You dont have enough money. Iron Rod's price is " , ironrod , " Dollars")
	elif Code == 3:
		if "Gold Rod" in ownboats:
			print("You already own Gold Rod")
		if tot_money >= goldrod:
			tot_money -= goldrod
			fishrod = "Gold Rod"
			ownrods.append("Gold Rod")
			print("You successfully bought Gold Rod!")
		else:
			print("You dont have enough money. Gold Rod's price is " , goldrod , " Dollars")


	#---------------------------------------------Boats---------------------------------------------


	elif Code == 11:
		if "Wooden Raft" in ownboats:
			print("You already own Wooden Raft")
		else:
			if tot_money >= woodenraft:
				tot_money -= woodenraft
				boat = "Wooden Raft"
				ownboats.append("Wooden Raft")
				print("You successfully bought Wooden Raft!")
			else:
				print("You dont have enough money. Wooden Raft's price is " , woodenraft , " Dollars")
	elif Code == 12:
		if "Wooden Boat" in ownboats:
			print("You already own Wooden Boat")
		else:
			if tot_money >= woodenboat:
				tot_money -= woodenboat
				boat = "Wooden Boat"
				ownboats.append("Wooden Boat")
				print("You successfully bought Wooden Boat!")
			else:
				print("You dont have enough money. Wooden Boat's price is " , woodenboat , " Dollars")
	elif Code == 13:
		if "Fishing Boat" in ownboats:
			print("You already own Fishing Boat")
		else:
			if tot_money >= fishingboat:
				tot_money -= fishingboat
				boat = "Fishing Boat"
				ownboats.append("Fishing Boat")
				print("You successfully bought Fishing Boat!")
			else:
				print("You dont have enough money. Fishing Boat's price is " , fishingboat , " Dollars")


	else:
		print("Please check your code.")


	save()

def b(Code):
	buy(Code)


def useRod(Code):
	global fishrod
	if Code == 1:
		fishrod = "Stone Rod"
		print("Your Rod has been changed to " , fishrod)
	elif Code == 0:
		fishrod = "Wooden Rod"
		print("Your Rod has been changed to " , fishrod)
	elif Code == 2:
		fishrod = "Iron Rod"
		print("Your Rod has been changed to " , fishrod)
	elif Code == 3:
		fishrod = "Gold Rod"
		print("Your Rod has been changed to " , fishrod)
	else:
		print("Please check your Code.")


	save()


def useBoat(Code):
	global boat
	if Code == 11:
		boat = "Wooden Raft"
		print("Your Rod has been changed to " , fishrod)
	elif Code == 10:
		boat = "Plastic Raft"
		print("Your Rod has been changed to " , fishrod)
	elif Code == 12:
		boat = "Wooden Boat"
		print("Your Rod has been changed to " , fishrod)
	elif Code == 13:
		boat = "Fishing Boat"
		print("Your Rod has been changed to " , fishrod)
	else:
		print("Please check your Code.")


	save()

def userod(Code):
	userod(Code)




class shop():
	def __init__(self):
		print("Welcome to the shop. You may buy upgrades here. Upgrades are given below."
			"\n"
			"\n1. FishingRods    [Do  shop.fr()   ]"
			"\n2. Boats          [Do  shop.boats()]"
			"\n3. Baits          [Do  shop.baits()]"
			"\n"
			"\nDo buy(Code) to buy something.")

	def fr():
		print("\nThere is a variety of Fishing Rods here."
			"\n"
			"\nNo.     Name              Price                    Code"
			"\n-------------------------------------------------------"
			"\n"
			"\n1.      Stone Rod         " , stonerod , " Dollars           1"
			"\n2.      Iron Rod          " , ironrod ,  " Dollars           2"
			"\n3.      Gold Rod          " , goldrod ,  " Dollars          3\n")

	def boats():
		print("\nThere are a few boats."
			"\n"
			"\nNo.     Name              Price                    Code"
			"\n-------------------------------------------------------"
			"\n"
			"\n1.      Wooden Raft       " , woodenraft ,  " Dollars           11"
			"\n2.      Wooden Boat       " , woodenboat ,  " Dollars          12"
			"\n3.      Fishing Boat      " , fishingboat , " Dollars         13\n")

		#
