#!/usr/bin/python3

# Read input from file

r = open("Day1-1Input.txt","r")
masses=r.readlines()

totalFuel = 0

def fuelNeeded(mass):
	return (mass//3)-2
	
def addFuelNeeded(fuel):
	
	incFuel = 0
	addFuel = fuelNeeded(fuel)
	while addFuel > 0:
		print(addFuel)
		incFuel += addFuel
		addFuel = fuelNeeded(addFuel)		
	return incFuel

for mass in masses:
	massInt=int(mass)
	
	# Divide by 3 (Round Down) and subtract 2
	fuel=fuelNeeded(massInt)
	additionalFuel = addFuelNeeded(fuel)
	totalFuel = totalFuel + fuel + additionalFuel
	print("Module: {0} Fuel: {1} Add Fuel: {2} ".format(totalFuel, fuel, additionalFuel))
	
print(totalFuel)



